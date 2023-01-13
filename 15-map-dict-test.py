def multiply_numbers(numbers):
    # Escribe tu solución 👇
    result = list(map(lambda x : x * 2, numbers))
    return result

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)


numbers_2 = [2, 4, 6, 8, 10]
response_2 = multiply_numbers(numbers_2)
print(response_2)