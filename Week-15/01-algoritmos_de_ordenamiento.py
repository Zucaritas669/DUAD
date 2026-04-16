# # Ordena de menor a mayor — de izquierda a derecha.

# def bubble_sort(list_of_sort):
#     for outer_index in range (0,len(list_of_sort)-1):
#         has_made_changes = False

#         for index in range(0,len(list_of_sort)-1-outer_index):
#             current = list_of_sort[index]
#             next = list_of_sort[index+1]

#             print(f'-- Iteracion {outer_index}, {index}. Elemento actual: {current}, Siguiente elemento: {next}')

#             if current > next:
#                 print('El elemento actual es mayor al siguiente. Intercambiandolos...')
#                 list_of_sort[index] = next
#                 list_of_sort[index + 1 ] = current
#                 has_made_changes = True

#           if not has_made_changes:
#               return

# my_test_list = [1, 2, 3, 10, 4, 5, 6, 7, 8]
# bubble_sort(my_test_list)

# print(my_test_list)


def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort) - 1):
        has_made_changes = False
        
        # Loop va de derecha a izquierda
        for index in range(len(list_to_sort) - 1, outer_index, -1):
            current_element = list_to_sort[index]
            previous_element = list_to_sort[index - 1]
            
            # Si el actual es MENOR al anterior — swap
            if current_element < previous_element:
                list_to_sort[index] = previous_element
                list_to_sort[index - 1] = current_element
                has_made_changes = True
        
        if not has_made_changes:
            return

my_test_list = [1, 2, 3, 10, 4, 5, 6, 7, 8]
bubble_sort(my_test_list)
print(my_test_list)