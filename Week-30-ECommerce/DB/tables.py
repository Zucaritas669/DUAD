from sqlalchemy import Integer,String, VARCHAR, Numeric ,ForeignKey , func
from sqlalchemy.orm import DeclarativeBase, Mapped , mapped_column ,relationship 

from decimal import Decimal
from datetime import datetime
from typing import Optional





#                    Creating tables on PostgreSQL using SQLALchemy / ORMs 

#======================================================================================
#                               class Base 
#======================================================================================
class Base(DeclarativeBase): #To use ORMs, we need to use/create a base class with "DeclarativeBase" as parameter and then inherit it to each sub class
    pass







#======================================================================================
#                               class User
#======================================================================================
class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema':'ECommerce_pets'}

    id : Mapped[int] = mapped_column(primary_key="True")
    name : Mapped[str] = mapped_column(VARCHAR(30))
    username : Mapped[str] = mapped_column(VARCHAR(35), unique=True)
    email : Mapped[str] = mapped_column(VARCHAR(45), unique=True)
    password : Mapped[str] = mapped_column(VARCHAR(255))
    role : Mapped[str] = mapped_column(VARCHAR(15)) # "user" as default

    #Relationships
    addresses = relationship("Address",back_populates="user")
    pay_methods = relationship("PayMethod",back_populates="user")
    invoices = relationship("Invoice",back_populates="user")
    carts = relationship("Cart",back_populates="user")






#======================================================================================
#                               class Address 
#======================================================================================
class Address(Base):
    __tablename__ = 'addresses'
    __table_args__ = {'schema':'ECommerce_pets'}

    id : Mapped[int] = mapped_column(primary_key="True")
    user_id : Mapped[int] = mapped_column(ForeignKey("ECommerce_pets.users.id"))
    address : Mapped[str] = mapped_column(VARCHAR(150))

    #Relationships
    user = relationship("User",back_populates="addresses")
    invoices = relationship("Invoice",back_populates="address")







#======================================================================================
#                               class PayMethod 
#======================================================================================
class PayMethod(Base):
    __tablename__ = 'pay_methods'
    __table_args__ = {'schema':'ECommerce_pets'}

    
    id : Mapped[int] = mapped_column(primary_key="True")
    user_id : Mapped[int] = mapped_column(ForeignKey("ECommerce_pets.users.id"))
    pay_method : Mapped[str] = mapped_column(VARCHAR(150))

    #Relationships
    user = relationship("User",back_populates="pay_methods")
    invoices = relationship("Invoice",back_populates="pay_method")







#======================================================================================
#                               class Category 
#======================================================================================
class Category(Base):
    __tablename__ = 'categories'
    __table_args__ = {'schema':'ECommerce_pets'}

    id : Mapped[int] = mapped_column(primary_key="True")
    name : Mapped[str] = mapped_column(VARCHAR(30))
    description : Mapped[Optional[str]] = mapped_column(VARCHAR(150))

    #Relationships
    items = relationship("Item",back_populates="category")







#======================================================================================
#                               class Item 
#======================================================================================
class Item(Base):
    __tablename__ = 'items'
    __table_args__ = {'schema':'ECommerce_pets'}

    id : Mapped[int] = mapped_column(primary_key="True")
    name : Mapped[str] = mapped_column(VARCHAR(30))
    category_id : Mapped[int] = mapped_column(ForeignKey("ECommerce_pets.categories.id"))
    stock : Mapped[int] = mapped_column(Integer)
    price : Mapped[Decimal] = mapped_column(Numeric(10,2))
    description : Mapped[Optional[str]] = mapped_column(VARCHAR(150))
    created_at : Mapped[datetime] = mapped_column(server_default=func.now()) # date auto
    is_active : Mapped[bool] = mapped_column(default=True)

    #Relationships
    invoice_items = relationship("InvoiceItem",back_populates="item")
    category = relationship("Category",back_populates="items")
    cart_items = relationship("CartItem", back_populates="item")







#======================================================================================
#                               class Invoice 
#======================================================================================
class Invoice(Base):
    __tablename__ = 'invoices'
    __table_args__ = {'schema':'ECommerce_pets'}

    id : Mapped[int] = mapped_column(primary_key="True")
    user_id : Mapped[int] = mapped_column(ForeignKey("ECommerce_pets.users.id"))
    pay_method_id : Mapped[int] = mapped_column(ForeignKey("ECommerce_pets.pay_methods.id"))
    address_id: Mapped[int] = mapped_column(ForeignKey("ECommerce_pets.addresses.id"))
    total : Mapped[Decimal] = mapped_column(Numeric(10,2))
    note : Mapped[Optional[str]] = mapped_column(VARCHAR(150))
    created_at : Mapped[datetime] = mapped_column(server_default=func.now()) # date auto

    #Relationships
    user = relationship("User",back_populates="invoices")
    address = relationship("Address",back_populates="invoices")
    pay_method = relationship("PayMethod",back_populates="invoices")
    invoice_items = relationship("InvoiceItem",back_populates="invoice")







#======================================================================================
#                               class Invoice Item 
#======================================================================================
class InvoiceItem(Base):
    __tablename__ = 'invoice_items'
    __table_args__ = {'schema':'ECommerce_pets'}

    id : Mapped[int] = mapped_column(primary_key="True")
    invoice_id : Mapped[int] = mapped_column(ForeignKey("ECommerce_pets.invoices.id"))
    item_id : Mapped[int] = mapped_column(ForeignKey("ECommerce_pets.items.id"))
    amount : Mapped[int] = mapped_column((Integer))
    unit_price : Mapped[Decimal] = mapped_column(Numeric(10,2))
    sub_total : Mapped[Decimal] = mapped_column(Numeric(10,2))
    note : Mapped[Optional[str]] = mapped_column(VARCHAR(150))
    created_at : Mapped[datetime] = mapped_column(server_default=func.now()) # date auto

    #Relationships
    invoice = relationship("Invoice",back_populates="invoice_items")
    returns = relationship("Return",back_populates="invoice_item")
    item = relationship("Item",back_populates="invoice_items")







#======================================================================================
#                               class Cart 
#======================================================================================
class Cart(Base):
    __tablename__ = 'carts'
    __table_args__ = {'schema':'ECommerce_pets'}

    id : Mapped[int] = mapped_column(primary_key="True")
    user_id : Mapped[int] = mapped_column(ForeignKey("ECommerce_pets.users.id"))
    status : Mapped[Optional[str]] = mapped_column(VARCHAR(15))

    #Relationships
    user = relationship("User",back_populates="carts")
    cart_items = relationship("CartItem",back_populates="cart")







#======================================================================================
#                               class Cart Item 
#======================================================================================
class CartItem(Base):
    __tablename__ = 'cart_items'
    __table_args__ = {'schema':'ECommerce_pets'}

    id : Mapped[int] = mapped_column(primary_key="True")
    cart_id : Mapped[int] = mapped_column(ForeignKey("ECommerce_pets.carts.id"))
    item_id : Mapped[int] = mapped_column(ForeignKey("ECommerce_pets.items.id"))
    quantity : Mapped[int] = mapped_column((Integer))

    #Relationships
    item = relationship("Item",back_populates="cart_items")
    cart = relationship("Cart",back_populates="cart_items")







#======================================================================================
#                               class Returns 
#======================================================================================
class Return(Base):
    __tablename__ = 'returns'
    __table_args__ = {'schema':'ECommerce_pets'}

    id : Mapped[int] = mapped_column(primary_key="True")
    invoice_item_id : Mapped[int] = mapped_column(ForeignKey("ECommerce_pets.invoice_items.id"))
    quantity : Mapped[int] = mapped_column((Integer))
    total_returned : Mapped[Decimal] = mapped_column(Numeric(10,2))
    returned_at : Mapped[datetime] = mapped_column(server_default=func.now()) # date auto

    #Relationships
    
    invoice_item = relationship("InvoiceItem",back_populates="returns")


