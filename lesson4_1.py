from sys import argv

name_sript, vyrabotka, stavka, premiya = argv

print("Название скрипта:", name_sript)
print("Выработка в часах:", vyrabotka)
print("Почасовая ставка:", stavka)
print("Премия:", premiya)
a = int(vyrabotka) * int(stavka) + int(premiya)
print("Итого зарплата: ", str(a))

