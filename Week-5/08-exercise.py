list_1 = []

for i in range(4):
    number = int(input(f'Type 4 random numbers\nInt number {i +1} ---> : '))
    list_1.append(number)
    print(list_1)

less = list_1[0]
for number in list_1:
    if number < less:
        less = number

print("Lista final:", list_1)
print("El valor mínimo es:", less)