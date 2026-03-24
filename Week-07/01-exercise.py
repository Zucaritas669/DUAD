def show_menu(actual_number):
    print('\n----CALCULATOR----')
    print(f'Actual number: {actual_number}')
    print('1 Addition')    
    print('2 Subtraction')     
    print('3 Multiplication')     
    print('4 Division')      
    print('5 Delete')
    print('6 Exit')


def get_number():
    while True:
        try:
            return float(input('Type a number--->'))
        except ValueError:
            print('Invalid number, Try again!!!')


def addition(actual , number):
    return actual + number


def subtraction(actual , number):
    return actual - number


def multiplication(actual , number):
    return actual * number


def division(actual , number):
    if number == 0:
        raise ZeroDivisionError
    return actual / number


def main():
    actual_number = 0


    while True:
        show_menu(actual_number)
        option = input('\n---Select an option----\n-> ')

        if option == '6':
            print('\n---Goodbye---')
            break

        elif option == '5':
            actual_number = 0
            print('\n---Elements deleted---')
            continue

        if option not in ['1','2','3','4']:
            print('\n---Invalid Option----')
            continue

        number = get_number()
        
        try:
            if option == '1':
                actual_number = addition(actual_number , number)
            elif option == '2':
                actual_number = subtraction(actual_number , number)
            elif option == '3':
                actual_number = multiplication(actual_number , number)
            elif option == '4':
                actual_number = division(actual_number , number)

            print(f'\n---Result:{actual_number}---')

        except ZeroDivisionError as ex:
            print(f'You cant divide by 0: {ex}')

main()