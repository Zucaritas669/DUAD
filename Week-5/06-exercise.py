number= [] 

list_1 = int(input('How many numbers do you want in the list?: '))

for i in range(list_1):
    user = int(input(f'int number {i +1} ---> : '))
    number.append(user)

print(f'Your list: {number}')

search = int(input('Which number do you want to count?  '))
count = number.count(search)

print(f"The number {search} appears {count} times.")