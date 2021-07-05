with open('text.txt') as f:
    lines = f.readlines()
    print("Количество строк в документе:", len(lines))
    for i, word in enumerate(lines, start=1):
        print("Количество слов в строке {}: {}".format(i, len(word.split())))



