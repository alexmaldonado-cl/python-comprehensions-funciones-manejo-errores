#Data Structure - set

#Sets = Conjuntos

# Se pueden modificar
# No tienen un orden
# No pueden tener elementos duplicados

def printLines():
    print('-' * 60)


printLines()

#creación de un conjunto de forma explicita
set_countries = {'col', 'cl', 'mex', 'bol', 'col'}
print(type(set_countries)) # <class 'set'>
print(set_countries)

printLines()

#el número 2 es omitido porque está repetido
set_numbers = {1, 2, 2, 3, 443, 23}
print(type(set_numbers))
print(set_numbers)

printLines()

# el output en consola cambiará el orden de los elementos
# num, str, bool, float ==> bool, num, str, float
set_types = {1, 'hola', False, 12.12}
print(type(set_types))
print(set_types)

printLines()

# creación de un conjunto a partir de un string
# el string será separado en caracteres, y se omitirán los que estén repetidos
set_from_string = set('hello')
print(type(set_from_string))
print(set_from_string)

printLines()

# creación de un conjunto a partir de una tupla
set_from_tuples = set(('abc', 'cbd', 'az'))
print(type(set_from_tuples))
print(set_from_tuples)

printLines()

# cracion de un conjunto a partir de una lista
list_numbers = [1, 2, 3, 4, 1, 2, 3, 4, 5]
set_from_list = set(list_numbers)
print(type(set_from_list))
print(set_from_list)

printLines()

# transformacion de un set a list
unique_numbers = list(set_from_list)
print(unique_numbers)