# Cree una clase de Circle con:
# Un atributo de radius (radio).
# Un método de get_area que retorne su área.


import math

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius**2)
    
get_radio = float(input("Radio -> "))

c = Circle(get_radio)

print(c.get_area())



        

    
    

        
