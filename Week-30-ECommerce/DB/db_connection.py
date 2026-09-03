import os
from dotenv import load_dotenv

load_dotenv()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URI = os.environ.get('DATABASE_URL')
engine = create_engine(DB_URI,echo=True)

try:
    connection = engine.connect()
    print("Connected Successful")
except Exception as ex:
    print("Error connecting the DB", ex)

Session = sessionmaker(bind=engine, expire_on_commit=False)
