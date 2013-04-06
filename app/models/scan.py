#coding=utf-8

from lib.base_model import *
from user import User

class Scan(BaseModel, ResourceMixin):
  """Scan Model"""

  __tablename__ = "scan"

  id = Column(Integer, primary_key=True)
  scan_started_at = Column(DateTime)
  scan_finished_at = Column(DateTime)
  scan_by_id = Column(ForeignKey(User.id))
  scan_by = relationship(User, uselist=False)
  findings = relationship("Finding")
  findings_num = Column(Integer, nullable=False)