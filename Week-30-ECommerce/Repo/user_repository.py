from DB.tables import User, Cart
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

        if user.is_active == False:
            return "User is deactivated"

        from Auth.jwt_handler import generate_token
        token = generate_token(user.id, user.role)
        return token


    @handle_session
    def edit_user(self, id, name, username, email, password, s=None):

        user = s.query(User).filter(User.id == id, User.is_active == True).first()
        if not user:
            print("User not found")
            return False

        if user.role == "admin":
            return "This is an admin account, only the developer can edit it"

        exist_username = s.query(User).filter(func.lower(User.username) == username.lower(), User.role != "admin",User.id != id, User.is_active == True).first()
        if exist_username:
            return "This username already exist"

        exist_email = s.query(User).filter(func.lower(User.email) == email.lower(),  User.role != "admin",User.id != id, User.is_active == True).first()
        if exist_email:
            return "This email already exist"

        new_password = generate_password_hash(password)

        user.name = name
        user.username = username
        user.email = email
        user.password = new_password
        s.commit()
        return True



    @handle_session
    def soft_delete_user(self, id, s=None):

        user = s.get(User,id)
        if not user:
            print("User not found")
            return False

        if user.role == "admin":
            return "This is an admin account, only the developer can delete it"


        has_a_cart = s.query(Cart).filter(Cart.user_id == id, Cart.status == "active").first()
        if has_a_cart:
            return "This user has an active Cart"


        user.is_active = False
        s.commit()
        return True




    @handle_session
    def reactive_user(self, id, s=None):

        user = s.get(User,id)
        if not user:
            print("User not found")
            return False

        if user.is_active == True:
            print("User is already active")
            return None

        user.is_active = True
        s.commit()
        return True


    


    
