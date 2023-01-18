try:
    print(0 / 0) #Error: ZeroDivisionError: division by zero
except Exception as error:
    print(error)

print('=' * 30)

try:
    assert 1 != 1, 'One is not equal to One'
except Exception as error:
    print(error)

print('=' * 30)

age = 10

try:
    if age < 18:
        raise Exception('No se permiten menores de edad')
except Exception as error:
    print(error)

print('=' * 30)

try:
    print(result)
except Exception as e:
    print(e)
else:
    result = 'Create en else block'
    print(result)
finally:
    print('Finally the try-except block')

print('=' * 30)