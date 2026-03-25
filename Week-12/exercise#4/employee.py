class Employee:
    def __init__(self,name,salary):
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name = value

    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,value):
        if value < 0:
            raise ValueError ("It must be greater than 0")
        else:
            self._salary = value
        

    def promote(self,percentage):
        self.salary += (self.salary * percentage /100)


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


e = Employee("Fio",get_int("Salary -> "))
print(e.name)
print(e.salary)
e.promote(get_int("Promotion % ")) 
print(e.salary)