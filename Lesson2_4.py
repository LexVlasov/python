# 4 задание
line = input('Введите слово:')
word = line.split()
for i, word in enumerate(word):
    print(i+1, word[:10]) if len(word) > 10 else print(i+1, word)

