import sys

vyrabotka, stavka, premiya = map(float, sys.argv[1:])

a = int(vyrabotka) * int(stavka) + int(premiya)
print("Итого зарплата: {}".format(a))

