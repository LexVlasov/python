# задание 7
import json

firm_dict = {}
average_profit = {}
total_list = []
with open('фирмы.txt', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        splitted_line = line.split()
        subject = splitted_line[0]
        profit = int(splitted_line[2]) - int(splitted_line[3])
        firm_dict[subject] = str(profit)
    average_profit['average profit'] = sum(int(x)for x in firm_dict.values())
    total_list.append(firm_dict)
    total_list.append(average_profit)
    print(firm_dict)
    print(average_profit)
    print(total_list)


with open('All.json', 'w', encoding='utf-8') as a:
    json.dump(total_list, a)
