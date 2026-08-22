from DB.tables import User
from sqlalchemy import func
from Repo.handle_session import handle_session

from werkzeug.security import generate_password_hash, check_password_hash


class UserRepository():
    @handle_session
    def register(self, name, username, email, password, role="user", s=None):
        user = s.query(User).filter(func.lower(User.email) == email.lower()).first()
        if user:
            print("Email already exist")
            return False

        user = s.query(User).filter(func.lower(User.username) == username.lower()).first()
        if user:
            print("Username already exist")
            return None

        hash_pass = generate_password_hash(password)
        user = User(
            name = name,
            username = username,
            email = email,
            password = hash_pass,
            role = role
        )
        s.add(user)
        s.commit()
        return True



#Use this function to create an admin
    def create_admin(self,name, username, email, password):
        result = self.register(
            name=name,
            username=username,
            email=email,
            password=password,
            role = "admin"
        )

        if result is False:
                print("Email already exist")
                return False

        if result is None:
            print("Username already exist")
            return None

        print(f"Admin '{username}' creado correctamente")
        return True




    
    @handle_session
    def login(self, email, password, s=None):
        user = s.query(User).filter(func.lower(User.email) == email.lower()).first()
        if not user or not check_password_hash(user.password , password):
            return False

        from Auth.jwt_handler import generate_token
        token = generate_token(user.id, user.role)
        return token








