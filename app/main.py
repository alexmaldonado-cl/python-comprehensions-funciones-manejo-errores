import utils

keys, values = utils.get_population()

print(keys, values)

print(utils.message)

data = [
    {
        'Country' : 'Chile',
        'Population' : '18'
    },
    {
        'Country' : 'Argentina',
        'Population' : '45'
    }
]

country = input('Type country => ')

result = utils.population_by_country(data, country)
print(result)