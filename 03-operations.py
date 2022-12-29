set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}
#? Unión de conjuntos
set_c = set_a.union(set_b)
print(set_c) #* {'col', 'mex', 'bol', 'pe'}
print(set_a | set_b)
#? Intersección de conjuntos
set_c = set_a.intersection(set_b)
print(set_c) #* {'bol'}
print(set_a & set_b)
#? Diferencia de conjuntos
set_c = set_a.difference(set_b)
print(set_c) #* {'col', 'mex'}
print(set_a - set_b)
#? Symetric Difference
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)