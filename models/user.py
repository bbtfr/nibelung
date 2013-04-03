#coding=utf-8

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from base_model import BaseModel, ResourceMixin
from config import session
from rbac.acl import Registry
from rbac.proxy import RegistryProxy
from rbac.context import IdentityContext, PermissionDenied

class User(BaseModel, ResourceMixin):
  """User Model"""

  __tablename__ = "user"

  id = Column(Integer, primary_key=True)
  username = Column(String, unique=True, nullable=False)
  password = Column(String(128), nullable=False)
  salt = Column(String(10), nullable=False)
  _roles = Column('roles', String, nullable=False, default="")

  @hybrid_property
  def roles(self):
    if self._roles: return self._roles.split(",")
    else: return []

  @roles.setter
  def set_roles(self, roles):
    if type(roles) == str: self._roles = roles
    elif type(roles) == list: self._roles = ",".join(roles)

  def authenticate(self, password):
    if not self.salt: return False
    return make_password(password, self.salt) == self.password

  @validates('username')
  def validate_username(self, key, value):
    if not value: self.errors[key] = '不能为空'
    elif len(value) < 5: self.errors[key] = '至少5个字符'
    elif key in self.errors: del self.errors[key]
    return value

  @validates('password')
  def validate_password(self, key, value):
    if not value: self.errors[key] = '不能为空'
    elif len(value) < 6: self.errors[key] = '至少6个字符'
    elif key in self.errors: del self.errors[key]
    return value

  def before_save(self):
    if not self.salt:
      self.salt = random_characters(10)
    self.password = make_password(self.password, self.salt)

  # querying
  @classmethod
  def find_by_username(cls, username):
    return session.query(cls).filter_by(username = username).first()

import hashlib, uuid
def random_characters(length):
  return uuid.uuid4().hex

def make_password(password, salt):
  return hashlib.sha512(password + salt).hexdigest()
