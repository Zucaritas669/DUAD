def bubble_sort(list_of_sort):
    iterations = 0
    changes = 0

    for outer_index in range(0,len(list_of_sort)-1):
        has_made_changed = False

        # Loop de izquierda a derecha
        for index in range(0,len(list_of_sort)-1-outer_index):
            current = list_of_sort[index]
            next = list_of_sort[index + 1]
            iterations += 1
            

            # Si el actual es MAYOR al siguente  — swap
            if current > next:
                list_of_sort[index] = next
                list_of_sort[index + 1] = current
                has_made_changed = True
                changes += 1
                

        if not has_made_changed:
            print(f"Iterations {iterations}: ")
            print(f"Changes {changes}: ")
            return

    print(f"Iterations {iterations}: ")
    print(f"Changes {changes}: ")
    
list_of_sort = [9,8,6,7,5,3,4,1,2]
bubble_sort(list_of_sort)
print(list_of_sort)
