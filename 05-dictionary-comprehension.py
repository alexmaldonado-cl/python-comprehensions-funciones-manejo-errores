def printLines():
    print('-' * 60)

dictionary = {}
for i in range(1, 11):
    dictionary[i] = i * 2


print(dictionary)

printLines()


dictionaryV2 = { i: (i+1) * 2 for i in range(0, 10) }
print(dictionaryV2)

printLines()

import random

countries = ['col', 'mex', 'bol', 'pe']
population = {}

for country in countries:
    population[country] = random.randint(1, 1000)

print(population)

printLines()

populationV2 = { country: random.randint(1, 1000) for country in countries }
print(populationV2)

printLines()

names = ['nico', 'zule', 'santi']
ages  = [12, 56, 98]

print(list(zip(names, ages))) # [('nico', 12), ('zule', 56), ('santi', 98)]

printLines()

newDictionary = { name: age for (name, age) in zip(names, ages) }
print(newDictionary) #{'nico': 12, 'zule': 56, 'santi': 98}