
# cd Week-27-ORMS 
# python models_db.py

from db import engine
from sqlalchemy import Integer, String, VARCHAR , ForeignKey

from typing import Optional
#Mapped automaticamente es not null, este import permite el null

# Import necesarios para trabajar orms con clases
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# DeclarativeBase tiene su propio MetaData internamente. Entonces en vez de:
#meta_obj.create_all(engine)

#AHORA
#meta_obj.create_all(engine)
# Table  se reemplaza por class User(Base) con __tablename__  /  __table_args__ = {'schema': '<schema name>'}
# Column se reemplaza por mapped_column
# MetaData() ya viene dentro de Base (Base.metadata)





#====================================== Class =================================

# 1. Create the base catalog by subclassing DeclarativeBase
class Base(DeclarativeBase):
    pass

# 2. Inherit from your base class to map a new database table
class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'lyfter_orm'}

    # Modern type-annotated columns
    id : Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(VARCHAR(50), unique=True)
    password: Mapped[str] = mapped_column(VARCHAR(50))

    addresses = relationship("Address", back_populates="user")
    cars = relationship("Car",  back_populates="user")
    #relationship() conecta dos modelos para acceder a otra tablas
    #primero usa el nombre de la calse
    #segundo el nombre del atributo 
    # Los nombres siempre se cruzan: User.addresses / Address.user



class Address(Base):
    __tablename__ = 'addresses'
    __table_args__ = {'schema': 'lyfter_orm'}

    id : Mapped[int]= mapped_column(primary_key=True)
    address : Mapped[str] = mapped_column(VARCHAR(50))
    user_id : Mapped[int] = mapped_column(ForeignKey("lyfter_orm.users.id"))

    user = relationship("User", back_populates="addresses")


class Car(Base):
    __tablename__ = 'cars'
    __table_args__ = {'schema': 'lyfter_orm'}

    id:Mapped[int] = mapped_column(primary_key=True)
    brand : Mapped[str] = mapped_column(VARCHAR(50))
    model : Mapped[str] = mapped_column(VARCHAR(50))
    year : Mapped[int] = mapped_column(Integer)
    user_id : Mapped[Optional[int]] = mapped_column(ForeignKey("lyfter_orm.users.id"))

    user = relationship("User",back_populates="cars")
    




