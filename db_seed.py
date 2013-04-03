from models import *
from config import engine

BaseModel.metadata.create_all(engine)

User(username='admin', password='secret').save()
