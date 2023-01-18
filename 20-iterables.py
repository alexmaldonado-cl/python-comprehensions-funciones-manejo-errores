for i in range(1, 10):
    print(i)

my_iter = iter(range(1, 4))
print(my_iter) #<range_iterator object at 0x000001EB6719BCD0>
print(next(my_iter))#1
print(next(my_iter))#2
print(next(my_iter))#3
print(next(my_iter)) #Error StopIteration