#!/usr/bin/env python
#coding=utf-8

from lib.base_model import BaseModel
from models import *
from config import engine

BaseModel.metadata.create_all(engine)
User(username='admin', password='secret', roles='admin').save()
