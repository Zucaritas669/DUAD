list_of_numbers = []

for i in range(4):
    num = int(input('type 4 numbers: '))
    list_of_numbers.append(num)

print(list_of_numbers)
print('The biggest number on the list is:', max(list_of_numbers))
print('The smallest number on the list is:', min(list_of_numbers))