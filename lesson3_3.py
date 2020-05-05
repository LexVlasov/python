def compare(num1, num2, num3):
    my_list = [num1, num2, num3]
    my_list.sort()
    return my_list[2]+my_list[1]

print(
    compare(
        num1=int(input("Введите первое число:")),
        num2=int(input("Введите второе число:")),
        num3=int(input("Введите третье число:"))
            )
     )