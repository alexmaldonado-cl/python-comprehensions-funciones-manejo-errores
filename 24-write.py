print('=' * 60)

'''
with open('./text.txt', 'r') as file: #file in read only mode
    for line in file:
        print(line)
    file.write('Where does it come from?') #ERROR => io.UnsupportedOperation: not writable
'''

'''
with open('./text.txt', 'w') as file: #write mode - Overwrites
    for line in file:
        print(line) #ERROR => io.UnsupportedOperation: not readable
    file.write('Where does it come from?')
'''

with open('./text.txt', 'r+') as file: #read and write mode
    for line in file:
        print(line)
    file.write('\nWhere does it come from?')

print('=' * 60)