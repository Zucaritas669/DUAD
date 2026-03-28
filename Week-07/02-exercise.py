def name():
    while True:
        try:
            name = input('Type a random name: ')   
            if name.isdigit():
                raise ValueError('Name cant be a number')
            return name
        except ValueError as ex:
            print(f'Error {ex}')
            

def get_age():
    while True:
        try: 
            age = int(input('Type your age: '))
            if age < 0:
                raise ValueError('Age must be positive')
            
            return age
        except ValueError as ex:
            print(f'Age must be positive: {ex}')

result_1 = name()
result_2 = get_age()

print(f'Your name is: {result_1} \nYour age is: {result_2}')