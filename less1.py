# a = 5
# b = a + 15
# print(a + b)

# a = input("Введите первое число:")
# b = input("Введите второе число:")
# print(int(a + b)**2)

# a = input("Введите имя:")
# b = input("Введите фамилию:")
# print(a + " " + b)

# a = input("Введите время в секунда:")
# s = int(a) % 60
# m = int(a) % 3600 //60
# h = int(a) // 3600
# print(str(h) + ':' + str(m) + ':' + str(s))

# n = input('Введите число:')
# print(int(n) + int(n + n) + int(n + n + n))

# a = input("Введите число от 0 до 1000:")
# i = 10
# while i < 101:
#     if int(a) > i:
#         h = int(a) // i
#         if h > i:
#             c = h // i
#             e = h % i // i
#             b = int(a) % i
#             if e > b and e > c:
#                 print(e)
#             elif b > e and b > c:
#                 print(b)
#             else: print(c)
#         else:
#             b = int(a) % i
#             if h > b:
#                 print(h)
#             else: print (b)
#     else: print(a)
#     break

# a = input("Введите сумму выручки:")
# b = input("Введите сумму издержки:")
# c = int(a) - int(b)
# d = c/int(a)
# if int(a) > int(b):
#     print("Компания имеет прибыль, с рентабельностью" + " " + str(d))
#     e = input("Введите кол-во работников:")
#     f = c / int(e)
#     print("Доход на одного сотрудника:" + str(f))
# else: print("Компания несет убытки")

a = int(input("Введите начальный результат:"))
b = int(input("Введите желаемый реузльтат:"))
i = 1
while a < b:
    a = a + a * 0.1
    i = i + 1
    print(str(i) + "-й день:" + str(a))