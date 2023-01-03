import random

countries = ['col', 'mex', 'bol', 'pe']

populationV2 = { country: random.randint(1, 100) for country in countries }
print(populationV2)

result = { country: population for (country, population) in populationV2.items() if population > 20 }

print(result)

text = 'Hola, mi nombre es Alex'
unique = { c: c.upper() for c in text if c in 'aeiou'}

print(unique)

textV2 = "Hola a todos, esta es una cadena de texto de prueba."
uniqueV2 = { c2: textV2.count(c2) for c2 in textV2 if c2 in 'aeiou' }
print(uniqueV2)