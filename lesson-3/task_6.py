# часть 1
def int_func(string):
    return string.title()
print(int_func("text"))

# часть 2
def title_func(string):
    list_title = []
    lst = string.split()
    for el in lst:
        list_title.append(int_func(el))
    print(*list_title)

my_str = input("Введите строку: ")
title_func(my_str)


