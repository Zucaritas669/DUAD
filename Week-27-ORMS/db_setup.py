from db import engine
from models_db import Base

Base.metadata.create_all(engine)
print("Tables Created")