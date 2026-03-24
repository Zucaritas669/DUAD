class BankAccount:
    def __init__(self):
        self.balance = 0 

    def deposit(self,money):
        self.balance += money

    def withdraw(self,money):
        if money > self.balance:
            print("Noy possible")
        else:
            self.balance -= money


class SavingsAccount(BankAccount):
    def __init__(self,min_balance):
        super().__init__()
        self.min_balance = min_balance
        
    def withdraw(self, money):
        if self.balance - money < self.min_balance:
            raise ValueError ("Invalid Founds")
        else:
            super().withdraw(money)



def get_int(prompt):
    while  True:
        try:
            int_ = int(input(prompt))
            if int_ < 0:
                raise ValueError ("Invalid amount")
            else:
                return int_
        except ValueError as ex:
            print(ex)

c = SavingsAccount(1000)
c.deposit(get_int("Deposit -> "))
print("-"*30)
c.withdraw(get_int("Withdraw -> "))
print(c.balance)