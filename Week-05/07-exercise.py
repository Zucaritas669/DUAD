list_1 = []
positive = True

for i in range(3):
    number = int(input(f'Type 3 random numbers\nInt number {i +1} ---> : '))
    list_1.append(number)
    print(list_1)

    if number <= 0:
        positive = False

if positive:
    print("Todos los números son positivos")
else:
    print("Hay números que NO son positivos")
