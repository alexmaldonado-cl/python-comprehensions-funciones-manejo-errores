numbers = [1, 2, 3, 4, 5, 6]
new_numbers = filter(lambda x : x % 2 == 0, numbers)
new_numbers = list(new_numbers)
print(numbers)
print(new_numbers)