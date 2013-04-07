#coding=utf-8

from lib.base_model import *
from scan import Scan

class Finding(BaseModel, ResourceMixin):
  """Finding Model"""

  __tablename__ = "finding"

  id = Column(Integer, primary_key=True)
  scan_id = Column(ForeignKey(Scan.id), nullable=False)
  scan = relationship(Scan, uselist=False)
  name = Column(Integer, nullable=False)
  severity = Column(Integer, nullable=False)
  message = Column(String, nullable=False)
  plugin_name = Column(String(128), nullable=False)
  plugin_group = Column(String(128), nullable=False)
  plugin_options = Column(String)
