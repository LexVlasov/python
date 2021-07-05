# задание 6
good = []
my_dict = {'Название': '', 'цена': '', 'кол-во': '', 'ед.': ''}
analitics = {'Название': [], 'цена': [], 'кол-во': [], 'ед.': []}
num = 0
while True:
    if input('Выход - Q, \nЛюбая клавиша - продолжить:').upper() == 'Q':
        break
    num += 1
    for f in my_dict.keys():
        user_data = input('{}:'.format(f))
        my_dict[f] = int(user_data) if (f == 'цена' or f == 'кол-во') else user_data
        analitics[f].append(my_dict[f])
    good.append((num, my_dict))
    print(good)
    print('Текущая аналитика по товарам:\n')
    for key, value in analitics.items():
        print(key, value)
