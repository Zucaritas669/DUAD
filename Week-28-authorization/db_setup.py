from db_tables import Base
from db_connection import engine

def create_db_tables():
    Base.metadata.create_all(engine)
    print("Tables created successful")

create_db_tables()

