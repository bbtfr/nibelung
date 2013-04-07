import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

base_dir =  os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
database_path = os.path.join(base_dir, 'db', 'database.db')
engine = create_engine('sqlite:///%s' % database_path, echo=False)
# engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
session = Session()
