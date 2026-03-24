class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return "Animal makes a sound"
    
class Dog(Animal):
    def speak(self):
        return "Guau"
    
class Cat(Animal):
    def speak(self):
        return "Miau"
    

def get_name(prompt):
    while True:
        name = input(prompt).strip()
        if name.replace(" ","").isalpha():
            return name
        else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        print("Invalid format")


def create_dog():
    return Dog(get_name("Dog name -> "))

def create_cat():
    return Cat(get_name("Cat name -> "))

dog = create_dog()
cat = create_cat()
print(dog.speak())  
print(cat.speak())
