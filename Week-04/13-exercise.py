numbers_list = []

for i in range (3):
    numbers = int(input(f"type number a number: "))
    numbers_list.append(numbers)
    counter += numbers #<- This counter is adding the number

print(f"{numbers_list}  Total: {counter}"  )

if (30 in  numbers_list or counter ==30):
    print("Correct")
else:
    print("Incorrect")