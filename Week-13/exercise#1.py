def decorator(func):
    def wrapper(*args,**kwargs):
        print(f"Parameters: {args}")
        result = func(*args,**kwargs)
        print(result)
    return wrapper

class Numbers:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    @decorator
    def sum(self):
        return self.num1 + self.num2
    

n = Numbers(15,27)
n.sum()




    

    




        





