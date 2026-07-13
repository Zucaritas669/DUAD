from sqlalchemy.orm import DeclarativeBase ,Mapped, mapped_column, relationship

from sqlalchemy import Integer, VARCHAR, Numeric ,String , ForeignKey, func
from decimal import Decimal
from datetime import datetime




class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema':'lyfter_fruit'}

    id:Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(VARCHAR(30))
    user_name : Mapped[str] = mapped_column(VARCHAR(30))
    email : Mapped[str] = mapped_column(VARCHAR(30), unique=True) 
    password :  Mapped[str] = mapped_column(VARCHAR(255))
    role : Mapped[str] =  mapped_column(VARCHAR(30)) # admin/user

    invoices = relationship("Invoice", back_populates = "user")


class Invoice(Base):
    __tablename__ = 'invoices'
    __table_args__ = {'schema':'lyfter_fruit'}

    id : Mapped[int] = mapped_column(primary_key=True)
    user_id : Mapped[int] = mapped_column(ForeignKey("lyfter_fruit.users.id"))
    total : Mapped[Decimal] = mapped_column(Numeric(10,2))
    created_at : Mapped[datetime] = mapped_column(server_default=func.now()) #Creates date auto 

    user = relationship("User", back_populates = "invoices")
    invoice_items = relationship("InvoiceItem", back_populates="invoice")
    

class Item(Base):
    __tablename__ = 'items'
    __table_args__ = {'schema':'lyfter_fruit'}

    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(VARCHAR(30))
    price : Mapped[Decimal] = mapped_column(Numeric(10,2))
    stock : Mapped[int] = mapped_column(Integer)
    entry_date : Mapped[datetime] = mapped_column(server_default=func.now())

    invoice_items = relationship("InvoiceItem", back_populates="item")

    

class InvoiceItem(Base):
    __tablename__ ='invoice_items'
    __table_args__ = {'schema':'lyfter_fruit'}

    id : Mapped[int] = mapped_column(primary_key=True)
    invoice_id : Mapped[int] = mapped_column(ForeignKey("lyfter_fruit.invoices.id"))
    item_id : Mapped[int] = mapped_column(ForeignKey("lyfter_fruit.items.id"))
    quantity : Mapped[int] = mapped_column(Integer)
    unit_price :Mapped[Decimal] = mapped_column(Numeric(10,2))
    sub_total :Mapped[Decimal] = mapped_column(Numeric(10,2))

    invoice = relationship("Invoice", back_populates="invoice_items")
    item = relationship("Item", back_populates="invoice_items")




