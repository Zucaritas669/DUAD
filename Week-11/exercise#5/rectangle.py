class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        if width < 0 or height < 0:
            raise ValueError("It must be greater than 0")

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2* (self.width * self.height)
    

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
            

def build_rectangle():
    return Rectangle(get_int("\nWidth -> "),get_int("\nHeight -> "))


r = build_rectangle()
print(r.get_area())
print(r.get_perimeter())






    
    
        

