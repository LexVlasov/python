# задание 7
from math import factorial
from itertools import count

def fibo_gen():
    a = int(input('Введите число:'))
    b = a
    for el in count(a):
        yield factorial(el), b
        b += 1
c = 0
for i, num in fibo_gen():
    print('Факториал {} - {}'.format(num, i))
    if c == 14:
        break
    c += 1