from db_tables import User, Invoice, Item, InvoiceItem
from db_connection import Session

def handle_session(func):
        def wrapper(*args,**kwargs):
                with Session() as s:
                    try:
                        return func(*args,s=s,**kwargs)                 
                    except Exception as ex:
                        s.rollback()
                        print("Data base error", ex)
                        return False
        return wrapper
                        
                                            


