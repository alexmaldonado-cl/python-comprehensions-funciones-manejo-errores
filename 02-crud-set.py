#creación de un conjunto de forma explicita
set_countries = {'col', 'cl', 'mex', 'bol', 'col'}
size = len(set_countries) # Length
print(type(set_countries)) # <class 'set'>
print(set_countries)
print(size)
print('col' in set_countries) # Search
print('pe' in set_countries) # Search


#* ADD

set_countries.add('pe')
print(set_countries)
print('pe' in set_countries) # Search

set_countries.add('pe')
print(set_countries)



#* UPDATE

set_countries.update({ 'ar', 'ecua', 'pe' })
print(set_countries)


#* REMOVE

set_countries.remove('col')
print(set_countries)

set_countries.remove('cl')
print(set_countries)

#set_countries.remove('arg') #Traceback ERROR
set_countries.discard('arg')
print(set_countries)

set_countries.discard('pe')
print(set_countries)

print(len(set_countries))
set_countries.clear(); #? Elimina todos los elementos
print(set_countries)
print(len(set_countries))