def int_func(lst_words):
    for i in lst_words:
        lst_words.append(lst_words[i])
    print(lst_words)

my_words = input("Введите слово: ").split()
int_func(my_words)

