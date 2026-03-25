class Swimmer:
    def swim(self):
        print(f"{self.name} is swimming")

class Flyer:
    def fly(self):
        print(f"{self.name} is flying")

class Duck(Swimmer, Flyer):
    def __init__(self, name):
        self.name = name

donald = Duck("Donald")
donald.swim()
donald.fly()