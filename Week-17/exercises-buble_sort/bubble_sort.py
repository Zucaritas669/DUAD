

def bubble_sort(list_of_sort):
    for outer_index in range (0,len(list_of_sort)-1):
        has_made_changes = False

        for index in range(0,len(list_of_sort)-1-outer_index):
            current = list_of_sort[index]
            next = list_of_sort[index+1]

            print(f'-- Iteracion {outer_index}, {index}. Elemento actual: {current}, Siguiente elemento: {next}')

            if current > next:
                print('El elemento actual es mayor al siguiente. Intercambiandolos...')
                list_of_sort[index] = next
                list_of_sort[index + 1 ] = current
                has_made_changes = True

        if not has_made_changes:
            return
