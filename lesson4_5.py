from functools import reduce

def my_func(a, b):
    return a * b

my_list = [num for num in range(100, 1001) if num % 2 == 0]
print(reduce(my_func, my_list))
