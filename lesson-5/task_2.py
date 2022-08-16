#Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
#подсчёт строк и слов в каждой строке.
import sys
my_f = open("test.txt", "r", encoding='utf-8')
for line in my_f:
    print(line,"Пробелов: ",line.count(" "))
my_f.close()