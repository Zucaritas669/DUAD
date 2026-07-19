from db_tables import User
from repositories.session import handle_session

from werkzeug.security import generate_password_hash, check_password_hash #Se usa para hash el password

class UserRepository():

    @handle_session
    def login(self, email, password, s=None):

        user = s.query(User).filter(User.email == email).first()

        if not user or not check_password_hash(user.password , password):
            return False
        
        # Si es válido, generar el token con su user_id y role
        from auth.jwt_handler import generate_token
        token = generate_token(user.id, user.role)

        return token


    @handle_session
    def get_user_email(self, email, s=None):
        user_email  = s.query(User).filter(User.email == email).first()
        if not user_email:
            print("Email not found")
            return False
        return user_email
    


    @handle_session
    def get_user_by_id(self, id , s=None):
        user = s.get(User, id)
        if not user:
            print("User not found")
            return False
        return user
        


    @handle_session
    def create_user(self, name, user_name, email, password, role, s=None ):
        
        user = s.query(User).filter(User.email == email).first()
        if user:
            print("Email already exist")
            return False
        
        hashed_pass = generate_password_hash(password)
        
        new_user = User(
            name = name,
            user_name = user_name,
            email = email,
            password = hashed_pass,
            role = role
        )
        s.add(new_user)
        s.commit()
        return True
    



    

    

        