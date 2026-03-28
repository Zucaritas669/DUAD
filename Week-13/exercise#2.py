def only_numbers(func):
    def wrapper(*args,**kwargs):
        for a in args:
            if not isinstance(a,(int,float)):
                raise ValueError ("Ops something went wrong, probably typed a str")
        result = func(*args,**kwargs)
        print(result) 
    return wrapper

@only_numbers
def sum(num1, num2):
    return num1 + num2

sum(15, 27)
