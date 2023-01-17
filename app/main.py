import utils

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

def run():

    keys, values = utils.get_population()

    print(keys, values)

    print(utils.message)

    country = input('Type country => ')

    result = utils.population_by_country(data, country)
    print(result)

#* Entry point
if __name__ == '__main__':
    run()