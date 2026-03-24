import random 
unknown_number = random.randint(1,10)

attempts = 0
counter = 0

while(attempts != unknown_number):
    attempts=int(input('Type a number between 1 and 10: '))
    counter = counter + 1

    if(attempts < unknown_number):
        print('You almost got it, try again: ') 
    elif(attempts > unknown_number):
        print('You almost got it,  try again: ')
    else:
        print('You have found the secret number!!')


print(f'You did {counter} attempts')