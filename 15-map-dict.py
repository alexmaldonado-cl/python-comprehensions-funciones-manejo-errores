import copy

tax = 1.19
items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalón',
        'price': 300
    },
    {
        'product': 'zapato',
        'price': 500
    }
]

items_cp = copy.deepcopy(items)

prices = list(map(lambda item : item['price'], items_cp))

def add_taxes(item):
    item['taxes'] = item['price'] * tax
    return item

new_items = list(map(add_taxes, items_cp))

print(items)
print('='*50)
print(items_cp)
print('='*50)
print(new_items)