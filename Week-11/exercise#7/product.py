class Product:
    def __init__(self,name,price,amount):
        self.name = name
        self.price = price
        self.amount = amount
        if self.price < 0 or self.amount < 0 :
            raise ValueError("It must be greater than 0")
    
class Inventory:
    def __init__(self):
        self.list_of_products = []

    def add_product(self,item):
        self.list_of_products.append(item)
    
    def show_product(self):
        for i in self.list_of_products:
            print(f"Name: {i.name}")
            print(f"Price: {i.price}")
            print(f"Amount: {i.amount}")

    def total(self):
        total = 0 
        for i in self.list_of_products:
            total += i.price * i.amount
        print(f"Total of the products ${total}")
        return total


def get_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number <= 0:
                print("\nInvalid Format")
            else:
                return number
        except ValueError as ex:
            print(f"Only numbers {ex}")


def valid_name():
    while True:
        name = input("Name ->").strip()
        if name.replace(" ","").isalpha():
            return name
        else:
            print("\nInvalid Format")


def add(inventory):
    p = Product(valid_name(), get_int("Price $"), get_int("Amount ->'"))
    inventory.add_product(p)

i = Inventory()
add(i)
i.show_product()
i.total()
