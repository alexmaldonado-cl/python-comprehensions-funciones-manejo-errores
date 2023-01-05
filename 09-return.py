def find_volume(length = 1, width = 1, depth = 1):
    return length * width * depth, width,  'hola';

result, width, text = find_volume(width=10)
print(type(result), result)
print(type(width), width)
print(type(text), text)
# print()