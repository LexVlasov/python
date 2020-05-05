# первый способ
def my_func(x, y):
    if x > 0 or y < 0:
        return x ** y
    else:
        return print("Х должен быть положительным, Y - отрицательным")

print(
    my_func(
        x=int(input("Введите положительное число:")),
        y=int(input("Введите отрицательное число:"))
           )
     )

# второй способ
def my_func(x, y):
    if x > 0 or y < 0:
        i = -1
        z = x
        while i > y:
            i = i - 1
            x = x * z
        return float(1/x)
    else:
        return print("Х должен быть положительным, Y - отрицательным")

print(
    my_func(
        x=int(input("Введите положительное число:")),
        y=int(input("Введите отрицательное число:"))
           )
     )