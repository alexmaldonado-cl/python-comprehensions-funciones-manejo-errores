'''
# Basic array
numbers = []

for element in range(1, 11):
    numbers.append(element)

print(numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# With list comprehensions

numbersV2 = [element * 2 for element in range(1, 11)] #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(numbersV2)
'''

numbers = []

for i in range(1, 11):
    if i % 2 == 0:
        numbers.append(i * 2)

print(numbers) # [4, 8, 12, 16, 20]

numbersV2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbersV2)