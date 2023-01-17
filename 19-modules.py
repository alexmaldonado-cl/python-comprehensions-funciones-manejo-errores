import sys

print(sys.path)

import re

text = 'My phone number is 311 123 121, the country code is 57 and my lucky number is 7'
result = re.findall('[0-9]+', text)
print(result)

import time

timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(timestamp)
print(local)
print(result)

import collections
numbers = [1, 2, 3, 44, 3, 3, 1, 2, 3, 4, 5, 4]
counter = collections.Counter(numbers)

print(counter)