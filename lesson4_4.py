my_list = [1, 2, 3, 4, 1, 2, 3, 5, 6, 0, 15, 10]
new_list = [num for num in my_list if my_list.count(num) == 1]
print(new_list)
