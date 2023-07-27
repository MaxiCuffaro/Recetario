###  Strigns ###

my_string = "mi_string"

my_other_string = "mi otro string"

print(len (my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "este es un string /n con salto de linea"
print(my_new_line_string)

### Formateo ###

name, surname, age = "maxi", "cuffa", 25
print("my nombre es {} {} y mi edad es {}".format(name, surname, age))
print("my nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"my nombre es {name} {surname} y mi edad es {age}")


###desempaquetado de caracteres ###
language = "python"
a, b, c, d, e, f = language
print(a)
print(b)


###Division###

language_slice = language[1:3] #Muestra caracter 1 y 3
print(language_slice)  


language_slice = language[1] #Muestra desde el caracter 1
print(language_slice)  

### reverse ###

language_slice = language[::-1] #Muestra la palabra al revez
print(reversed_language)  

####Funciones###

print(language.capitalize())  # para poner la primera letra en mayuscula
print(language.upper()) # todo mayuscula
print(language.count("t")) #cuantas t tiene
print(language.isnumeric()) #si es un numero true o false
print(language.lower()) # todas minusculas


