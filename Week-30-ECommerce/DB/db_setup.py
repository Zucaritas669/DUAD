from DB.tables import Base
from DB.db_connection import engine

def create_tables():
    Base.metadata.create_all(engine)
    print("Tables created Successful")
    
if __name__ == "__main__":
    create_tables()

#python -m DB.db_setup