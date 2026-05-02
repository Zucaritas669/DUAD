from models import User
from datetime import datetime

#-------------- custom decorator / login_required ------------------
def login_required(func):
    def wrapper(self,*args,**kwargs):
        if not self.current_user:
            raise ValueError("user not found")
        else:
            return func(self,*args,**kwargs)
    return wrapper

#lOGIC App
#===================== Class PocketLedger =====================
class PocketLedger:
    def __init__(self):
        self.user_list = []
        self.categories_list = []
        self.movements_list = []
        self.current_user = None


#--------------------- Find, create,login and change password methods --------------------------
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
    
    def delete_category(self,name):
        for c in self.categories_list:
            if c.name == name:
                self.categories_list.remove(c)
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
    

#--------------------- Add methods --------------------------
    @login_required
    def add_category(self,category):
        self.categories_list.append(category)

    @login_required
    def add_expense(self,expense):
        self.movements_list.append(expense)

    @login_required
    def add_income(self,income):
        self.movements_list.append(income)


#--------------------- filter methods --------------------------

    def filter_by_date(self, start_date, end_date):
        start = datetime.strptime(start_date, "%d/%m/%Y")
        end = datetime.strptime(end_date, "%d/%m/%Y")
        
        dates_list = []

        for m in self.movements_list:
            m_date = datetime.strptime(m.date,"%d/%m/%Y" )
            if start <= m_date <= end:
                dates_list.append(m)
        return dates_list

#--------------------- get methods -------------------------

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




