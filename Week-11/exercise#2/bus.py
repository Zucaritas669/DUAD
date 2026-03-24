class Person:
    def __init__(self,name):
        self.name = name

class Bus:
    def __init__(self,max_passengers):
        self.max_passengers = max_passengers
        self.passengers_list= []

    def add_passenger(self,passenger):
        if len(self.passengers_list) < self.max_passengers:
            self.passengers_list.append(passenger)
        else:
            print("This bus in Full; Please wait for tne next one")

    def remove_passenger(self,passenger):
                if passenger in self.passengers_list:
                    self.passengers_list.remove(passenger)
                else:
                    print("The passenger is not in the bus")


def valid_name():
    while True:
        name = input("Name ->").strip()
        if name.replace(" ","").isalpha():
            return name
        else:
            print("\nInvalid Format")
        

def add(bus):
    for i in range(bus.max_passengers):
        person = Person(valid_name())
        bus.add_passenger(person)


def kick(bus):
    name = input("Kick -> ")
    for i in bus.passengers_list:
        if i.name == name:
            bus.remove_passenger(i)
            break

b = Bus(int(input("MAX PASSENGERS -> ")))
add(b)
kick(b)
                    

    

        


        








    

