from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'
engine = create_engine(DB_URI , echo=True)

try:
    connection = engine.connect()
    print("Connected successful")
except Exception as ex:
    print("Error connecting the DB",ex)

Session = sessionmaker(bind=engine , expire_on_commit=False)

