from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import validates, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.exc import IntegrityError
from config import session

BaseModel = declarative_base()

class ResourceMixin(object):
  def __eq__(self, other):
    return hasattr(other, "id") and self.id == other.id

  def __hash__(self):
    return hash(self.id)

  def before_save(self):
    pass

  errors = {}
  def save(self):
    self.before_save()
    try:
      if 'SQL' in self.errors: del self.errors['SQL']
      if len(self.errors) > 0: return False
      session.add(self)
      session.commit()
      return True
    except IntegrityError, e:
      self.errors['SQL'] = e.message
      return False

  def destroy(self):
    try:
      session.delete(self)
      session.commit()
      return True
    except IntegrityError, e:
      self.errors['SQL'] = e.message
      return False

  @classmethod
  def all(cls):
    return session.query(cls).all()

  @classmethod
  def find_by(cls, **filter):
    return session.query(cls).filter_by(**filter).first()