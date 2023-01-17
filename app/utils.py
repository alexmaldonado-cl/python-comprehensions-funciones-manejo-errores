
def get_population():
    keys = ['cl', 'arg', 'mx']
    values = [18, 45, 120]
    return keys, values

def population_by_country(data, country):
    result = filter(lambda item : item['Country'] == country, data)
    result = list(result)
    return result

message = 'Hello World'