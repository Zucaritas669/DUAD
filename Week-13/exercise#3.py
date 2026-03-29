from datetime import date




class User:
    def __init__(self,date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )
    
def only_adults(func):
    def wrapper(user,*args,**kwargs):
        if user.age < 18:
            raise ValueError(f"{user.age} must be greater than 0") 
        func(user,*args,**kwargs)
    return wrapper

@only_adults
def buy_drugs(user):
    print("Drugs have been gotten")


u = User(date(2000, 1, 1))
buy_drugs(u)


    



