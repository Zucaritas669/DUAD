my_string = 'Pizza con piña y coca, queque y una piñata'

for i in range(len(my_string) - 1, -1, -1 ):
    print(my_string[i])
    
    # LOS -1 SON PARA: len(my_string) - 1 → calcula automáticamente el último índice, sin importar si hay 5 letras o 200.
    #-1 → siempre se usa como límite para detenerse justo antes del índice 0.
    #-1 → siempre es el paso negativo para ir hacia atrás.
    
    