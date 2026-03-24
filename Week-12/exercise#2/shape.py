from abc import ABC , abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
        


class Square(Shape):
    def __init__(self,side):
        self.side = side

    def calculate_perimeter(self):
        return 4 * self.side
    
    def calculate_area(self):
        return self.side ** 2
    

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2*(self.width + self.height)
    
    def calculate_area(self):
        return self.width * self.height
    


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


circle = Circle(get_int("Radius -> "))
print(circle.calculate_area())
print(circle.calculate_perimeter())
print("-"*30)

square = Square(get_int("Side ->"))
print(square.calculate_perimeter())
print(square.calculate_area())
print("-"*30)

rectangle = Rectangle(get_int("Width -> "),get_int("Height ->"))
print(rectangle.calculate_perimeter())
print(rectangle.calculate_area())



