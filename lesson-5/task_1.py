#Создать программный файл в текстовом формате, записать в него построчно данные,
#вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
#строка
import sys
my_string = input("Введите слова через пробел: ").split()
my_f = open("user.txt", "w", encoding='utf-8')
for el in range(len(my_string)):
    my_f.write(my_string[el] + "\n")
my_f.close()
my_f = open("user.txt", "r", encoding='utf-8')
content = my_f.read()
print(content)
my_f.close()
