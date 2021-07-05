# Задание 5
def my_func():
    summary = 0
    while True:
        i = 0
        value = 0
        value = list(map(str, input("Введите число или Q для выхода:").split()))
        if value[(len(value)-1)] == 'Q' or value[(len(value)-1)] == 'q':
            if len(value) == 1:
                break
            else:
                while i < (len(value)-1):
                    summary = int(value[i]) + summary
                    i = i + 1
                break
        else:
            while i < len(value):
                summary = int(value[i]) + summary
                i = i + 1
            print(summary)
            continue
    return summary


result = my_func()
print("Вы вышли. Сумма равняется " + str(result))
