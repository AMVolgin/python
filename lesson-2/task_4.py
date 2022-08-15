my_words = input("Введите слова через пробел: ").split()
for i in my_words:
    if len(i) <= 10:
        print(i)
    else:
        print(i[:10])
