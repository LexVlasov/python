# задание 6
def int_func():
    i = 0
    s = 'Текст:'
    value = list(map(str, input("Введите текст:").split()))
    while i < len(value):
        print(s)
        s = value[i].title()
        i = i + 1
    return s

print(int_func())