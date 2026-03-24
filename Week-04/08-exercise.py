counter  = 1
plus = 0 

number = int(input('Type a random number: '))
while(counter <= number):
    plus += counter
    counter += 1

print(f'The result this addition is: {plus} ')