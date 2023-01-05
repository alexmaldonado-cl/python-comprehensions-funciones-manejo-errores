import random

countries = ['col', 'mex', 'bol', 'pe']

population_v2 = { country: random.randint(1, 100) for country in countries }
print(population_v2)

result = { country: population for (country, population) in population_v2.items() if population > 20 }

print(result)

text = 'Hola, mi nombre es Alex'
unique = { c: c.upper() for c in text if c in 'aeiou'}

print(unique)

text_v2 = "Hola a todos, esta es una cadena de texto de prueba."
unique_v2 = { c2: text_v2.count(c2) for c2 in text_v2 if c2 in 'aeiou' }
print(unique_v2)