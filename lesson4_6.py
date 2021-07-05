# задание 6
# a
from itertools import count, cycle

for i in count(int(input('Введите число:'))):
    print(i)

# b
my_list = [num for num in range(1, 15)]
for el in cycle(my_list):
    print(el)

