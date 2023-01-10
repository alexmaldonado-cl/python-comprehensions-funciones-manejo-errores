def increment(x):
    return x + 1

result = increment(10)
print(result)

#func = lambda args : return val
# 

increment_v2 = lambda x : x + 1

result = increment_v2(20)
print(result)

full_name = lambda name, lastname : f'Fullname is {name.title()} {lastname.title()}'
print(full_name('alex', 'maldonado'))


# Lamdba - Basic
lambda_func = lambda x : x**2
print(lambda_func(3))
print(lambda_func(4))

# Lamdba - Intermediate
lambda_func = lambda x: True if x**2 >= 10 else False
print(lambda_func(3))
print(lambda_func(4))


# Lambda - Advance

# n = 1 M.Aritmetica / 2 M.Geometrica / 3 M.Armonica"
# No se puede definir el "elif" dentro de una funcion lamdba
lambda_func = lambda  x,y,z,n : (x+y+z)/3 if n == 1 else ( (x*y*z)**(1/3) if n == 2 else (3/((1/x)+(1/y)+(1/z)))) 
print('Media Aritmética => ' + str(lambda_func(4,5,6,1)))
print('Media Geométrica => ' + str(lambda_func(4,5,6,2)))
print('Media Armónica => ' + str(lambda_func(4,5,6,3)))