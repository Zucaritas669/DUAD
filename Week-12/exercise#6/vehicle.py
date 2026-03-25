class Vehicle:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year


    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self,value):
        if not value:
            raise ValueError("Brand can not be empty")
        self._brand  = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self,value):
        if value < 1900:
            raise ValueError("The car can not be that old")
        self._year = value



    def get_info(self):
        return  f"Brand: {self._brand} | Year: {self._year}"
        


class Car(Vehicle):
    def __init__(self, brand, year,doors):
        super().__init__(brand, year,)
        self.doors = doors


    def get_info(self):
        return super().get_info() + f"| Doors: {self.doors}"


class Motorcycle(Vehicle):
    def __init__(self, brand, year,type_):
        super().__init__(brand, year)
        self.type_ = type_

    def get_info(self):
        return super().get_info() + f"| Type: {self.type_}"




#--------------------- get info -------------------------------
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

def get_text(prompt):
    while  True:
            text = input(prompt).strip()
            if text.replace(" ","").isalpha():
                return text
            else:
                print("Invalid text")


car = Car(get_text("Brand -> "),get_int("Year -> "),get_int("Doors -> "))
print(car.get_info())
moto = Motorcycle(get_text("Brand -> "), get_int("Year -> "), get_text("Type -> "))
print(moto.get_info())