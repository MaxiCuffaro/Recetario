#variables en minusculas

my_variable = 'My string variable'
print (my_variable)

my_int_variable = 5
print (my_int_variable)

my_bool_variable = False
print (my_bool_variable)

my_int_to_str_variable = str (my_int_variable)
print (my_int_to_str_variable)
print (type (my_int_to_str_variable))

#Concatenacion de variables en un print 
print(my_int_variable, my_bool_variable, my_variable)
print ('este es el valor de :', my_bool_variable)

# Funciones del sistema
print(len(my_variable))

#Variables en una sola linea
name, surname, alias, age = "maxi", 'Cuffa', 'cuffita', 'age'



#inputs = NOS PIDE DATOS POR TECLADO  
first_name = input ( "cual es tu nombre ?")
age = input (" cuantos años tienes?")
print(name)
print(age)

# Forzamos el tipado  
address: str = "Mi direccion "
address = 32 
print (type (address))