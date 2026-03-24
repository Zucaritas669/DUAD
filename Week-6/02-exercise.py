# Intente accesar a una variable definida dentro de una función desde afuera.
# 
# def my_function():
#     local_var = "Soy local"
#     print("Dentro de la función:", local_var)

# my_function()


# print("Fuera de la función:", local_var)




# Intente accesar a una variable global desde una función y cambiar su valor.

# global_var = 10  

# def modify_global():
#     global global_var  
#     global_var += 5
#     print("Dentro de la función:", global_var)

# print("Antes de la función:", global_var)
# modify_global()
# print("Después de la función:", global_var)