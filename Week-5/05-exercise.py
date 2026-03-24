found_number = []

for i in range(10):
    print('Type 10 number')
    number = int(input(f'#{i + 1}: '))
    found_number.append(number)

print(f'The biggest number is: {max(found_number)}')