
from models import User, Category,Movement

def find_email(self,email):
        for e in self.user_list:
            if e.email == email:
                return e
        return False
    

def find_user(self,email,password):
    for e in self.user_list:
        if e.email == email and e.password == password:
            return e
    return False
    
def find_category(self,name):
    for c in self.categories_list:
        if c.name == name:
            return c
    return False
    

def create_user(self,name,email,password):
        if not self.find_email(email):
            new_user = User.create_user(name,email,password)
            self.user_list.append(new_user)
            return True
        else:
            return False
        

def login(self,email,password):
        user = self.find_email(email)
        if user and user.password == password:
            self.current_user = user
            return True
        return False
    
    
def change_password(self,email,password):
        user = self.find_email(email)
        if user and user.password != password:
            user.password = password
            return True
        return False


def get_total(self):

        total_income = 0
        total_expense = 0

        for m in self.movements_list:
            if m.movement_type == "income":
                total_income += m.amount
            else:
                total_expense += m.amount

        balance = total_income -total_expense
        return total_income, total_expense, balance
