
def name(prompt):
    while True:
        name = input(prompt).strip()
        if name.replace(" ","").isalpha():
            return name
        print("\n⚠︎ Invalid format; Please try again ⚠︎")


def repeat_twice (func):
    def wrapper(*arg,**kwargs):
        for r in range(2):
            func(*arg,**kwargs)
    return wrapper

@repeat_twice
def greeting():
    print(f"Hello {name("NAME ->")}")

greeting()