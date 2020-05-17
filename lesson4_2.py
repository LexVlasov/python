my_list = [1, 3, 2, 4, 10, 5, 25, 15, 8, 99]
new_list = [num for i, num in enumerate(my_list) if my_list[i] > my_list[i-1] and i != 0]
print(new_list)