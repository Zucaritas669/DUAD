from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



DB_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'
engine = create_engine(DB_URI, echo=True)

try:
    connection = engine.connect()
    print("Connected Successful !!")
except Exception as ex:
    print("Could not connect to the DB", ex)


Session = sessionmaker(bind=engine)
# crea sesiones conectada al engine
# cada vez que hagamos Session() se abre una sesión nueva para ejecutar queries