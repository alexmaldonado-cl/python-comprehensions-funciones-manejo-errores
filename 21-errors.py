# print(0 / 0) #Error: ZeroDivisionError: division by zero
# print(result) #Error: NameError: name 'result' is not defined

print('Hello')

suma = lambda x, y : x + (y * 2)
assert suma(2, 2) == 4 #Error: AssertionError

print('Hello #2')

age = 10

if age < 18:
    raise Exception('No se permiten menores de edad') #Exception: No se permiten menores de edad