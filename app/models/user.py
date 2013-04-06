#coding=utf-8

from lib.base_model import *
from datetime import datetime

class User(BaseModel, ResourceMixin):
  """User Model"""

  __tablename__ = "user"

  id = Column(Integer, primary_key=True)
  username = Column(String, unique=True, nullable=False)
  encrypted_password = Column(String(128), nullable=False)
  salt = Column(String(10), nullable=False)
  _roles = Column('roles', String, nullable=False, default="")

  created_at = Column(DateTime)
  updated_at = Column(DateTime)

  _current_user = None

  def authenticate(self, password):
    if not self.salt: return False
    if make_password(password, self.salt) == self.encrypted_password:
      self.__class__._current_user = self
      return True
    else:
      return False

  @property
  def roles(self):
    if self._roles: return self._roles.split(",")
    else: return []

  @roles.setter
  def roles(self, value):
    if type(value) == str: self._roles = value
    elif type(value) == list: self._roles = ",".join(value)

  @property
  def password(self):
    return self._password

  @password.setter
  def password(self, password):
    self._password = self.validate_password('password', password)
    if not self.salt:
      self.salt = random_characters(10)
    self.encrypted_password = make_password(self.password, self.salt)
  
  @hybrid_property
  def password_confirm(self):
    return self._password_confirm

  @password_confirm.setter
  def password_confirm(self, password_confirm):
    self._password_confirm = self.validate_password_confirm('password_confirm', password_confirm)

  @validates('username')
  def validate_username(self, key, value):
    if key in self.errors: del self.errors[key]
    if not value: self.errors[key] = u'用户名不能为空'
    elif len(value) < 3: self.errors[key] = u'用户名至少3个字符'
    elif not self.id and User.find_by_username(value) != None: 
      self.errors[key] = u'用户%s已存在' % value
    return value

  @validates('password')
  def validate_password(self, key, value):
    if key in self.errors: del self.errors[key]
    if hasattr(self, key):
      if not value: self.errors[key] = u'密码不能为空'
      elif len(value) < 6: self.errors[key] = u'密码至少6个字符'
    return value

  @validates('password_confirm')
  def validate_password_confirm(self, key, value):
    if key in self.errors: del self.errors[key]
    if value != self.password:
      self.errors[key] = u'两次输入密码不一致'
    return value

  def before_save(self):
    if not self.created_at:
      self.created_at = datetime.now()
    self.updated_at = datetime.now()

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
