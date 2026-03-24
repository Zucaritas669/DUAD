list_of_numbers = []

for i in range(3):
    num = int(input('type 3 numbers: '))
    list_of_numbers.append(num)

print(list_of_numbers)
print('The biggest number on the list is:', max(list_of_numbers))