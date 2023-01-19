# file = open('./text.txt')
# print(file.read())

print('=' * 50)
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# for line in file:
#     print(line)

with open('./text.txt', 'r') as file: #file in read only mode
    for line in file:
        print(line)

# Write-Overwrites
# with open('./text.txt', 'w') as f: #write data to a file
#     data = 'some data to be written to the file'
#     f.write(data)

# Append-adds at last
with open('./text.txt', 'a') as f:  # append mode
    new_line = '\n'
    data     = 'Some data to be written to the file'
    f.write(new_line)
    f.write(data)
    f.write(new_line)

print('=' * 50)

# file.close()