
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,11, 11, 11, 11]
list_num = []

for num in range(len(my_list) -1, -1, -1):
    if my_list [num] %2 != 0 :
        list_num.append(my_list[num])
        my_list.pop(num)
    
print(f'Deleted numbers {list_num} and the new list: {my_list}' )
