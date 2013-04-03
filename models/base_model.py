from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
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
    try:
      if 'SQL' in self.errors: del self.errors['SQL']
      if len(self.errors) > 0: return False
      self.before_save()
      session.add(self)
      session.commit()
      return True
    except IntegrityError, e:
      self.errors['SQL'] = e.message
      return False
