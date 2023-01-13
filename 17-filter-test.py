def filter_by_length(words):
   result = filter(lambda word : len(word) >= 4, words)
   result = list(result)
   return result

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)