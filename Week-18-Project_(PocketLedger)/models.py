import re


#====================== Class User ===================
class User:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self._password = password

#---------- get password and change it --------------
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,new_password):
        if re.match(r'^(?=.*\d).{8,}$',new_password): #To change password if the user forgets it
            self._password = new_password
        else:
            raise ValueError("Invalid Format")


    @classmethod
    def create_user(cls,name,email,password):
        return cls(name,email,password)


#====================== Class Category ===================
class Category:
    def __init__(self,name,color="#FFFFFF"):
        self.name = name
        self.color = color


    @classmethod
    def create_category(cls,name,color):
        return cls(name,color)
    

#====================== Class Movement ===================
class Movement:
    def __init__(self,title,amount,category,movement_type,date):
        self.title = title
        self.amount = amount
        self.category = category   #Object Category
        self.movement_type = movement_type  # expense or income
        self.date = date


    @classmethod
    def create_movement(cls,title,amount,category,movement_type,date):
        return cls(title,amount,category,movement_type,date)





