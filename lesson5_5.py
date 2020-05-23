# задание 5

with open('набор чисел.txt', 'w', encoding='utf-8') as f:
    numb = int(input("Введите начальное число:"))
    cnt = int(input("Введите конечное число:"))
    sum = 0
    for i in range(numb, cnt+1):
        f.write('Полученное число: ' + str(i) + '\n')
        sum = sum + i
    f.write('Сумма чисел равна: ' + str(sum))
    print('Все записано в файл')

# with open('набор чисел.txt', 'w', encoding='utf-8') as f:
#     nums = input('Введите числа через пробел:')
#     f.write('Введеные числа: ' + nums + '\n')
#     nums = map(int, nums.split())
#     sum_nums = sum(nums)
#     f.write('Сумма чисел равна: ' + str(sum_nums))
# print('Все записано в файл')
