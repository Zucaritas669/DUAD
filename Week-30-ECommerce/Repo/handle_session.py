from DB.db_connection import Session

def handle_session(func):
    def wrapper(*args, **kwargs):
        with Session() as s:
            try:
                return func (*args, **kwargs , s=s)
            except Exception as ex:
                print(f"Error handle the session: {ex}")
                s.rollback()
                raise
            
    return wrapper