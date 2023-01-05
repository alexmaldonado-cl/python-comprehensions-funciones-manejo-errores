def print_lines():
    print('-' * 60)

dictionary = {}
for i in range(1, 11):
    dictionary[i] = i * 2


print(dictionary)

print_lines()


dictionary_v2 = { i: (i+1) * 2 for i in range(0, 10) }
print(dictionary_v2)

print_lines()

import random

countries = ['col', 'mex', 'bol', 'pe']
population = {}

for country in countries:
    population[country] = random.randint(1, 1000)

print(population)

print_lines()

populationV2 = { country: random.randint(1, 1000) for country in countries }
print(populationV2)

print_lines()

names = ['nico', 'zule', 'santi']
ages  = [12, 56, 98]

print(list(zip(names, ages))) # [('nico', 12), ('zule', 56), ('santi', 98)]

print_lines()

new_dictionary = { name: age for (name, age) in zip(names, ages) }
print(new_dictionary) #{'nico': 12, 'zule': 56, 'santi': 98}