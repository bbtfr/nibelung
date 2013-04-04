#coding=utf-8

from base_model import *

class User(BaseModel, ResourceMixin):
  """User Model"""

  __tablename__ = "user"

  id = Column(Integer, primary_key=True)
  username = Column(String, unique=True, nullable=False)
  password = Column(String(128), nullable=False)
  salt = Column(String(10), nullable=False)
  _roles = Column('roles', String, nullable=False, default="")

  def roles():
    doc = "The roles property."
    def fget(self):
      if self._roles: return self._roles.split(",")
      else: return []
    def fset(self, value):
      if type(value) == str: self._roles = value
      elif type(value) == list: self._roles = ",".join(value)
    return locals()
  roles = property(**roles())

  def authenticate(self, password):
    if not self.salt: return False
    if make_password(password, self.salt) == self.password:
      self.__class__._current_user = self
      return True
    else:
      return False

  @validates('username')
  def validate_username(self, key, value):
    if not value: self.errors[key] = u'不能为空'
    elif len(value) < 5: self.errors[key] = u'至少5个字符'
    elif key in self.errors: del self.errors[key]
    return value

  @validates('password')
  def validate_password(self, key, value):
    if not value: self.errors[key] = u'不能为空'
    elif len(value) < 6: self.errors[key] = u'至少6个字符'
    elif key in self.errors: del self.errors[key]
    return value

  def before_save(self):
    if not self.salt:
      self.salt = random_characters(10)
    self.password = make_password(self.password, self.salt)

  # querying
  @classmethod
  def find_by_username(cls, username):
    return cls.find_by(username=username)

  @classmethod
  def current_user(cls):
    return cls._current_user

import hashlib, uuid
def random_characters(length):
  return uuid.uuid4().hex

def make_password(password, salt):
  return hashlib.sha512(password + salt).hexdigest()
