def sum_values(list_of_things):
    total = 0
    new_list= []

    for i in list_of_things:
        try:
            num = float(i)
            new_list.append(num)
            total += num
            print(f'{num}:Added correctly')
        except ValueError as ex:
            print(f'{i}:Invalid element')

    return new_list, total
            
things = ['10', 'manzana', '5.5', '3', 'n/a'] 

value, total = sum_values(things)

print("\nInvalid Values:", value)
print("Total:", total)