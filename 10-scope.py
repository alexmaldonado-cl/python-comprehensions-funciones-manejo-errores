price = 100 #* global scope

def increment():
    price = 200 #? local
    result = price + 10 #? local
    return result

print(price)
price_2 = increment()
print(price_2)