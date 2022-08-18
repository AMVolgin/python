#Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
#пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

import sys
with open("dig.txt", "w" , encoding='utf-8') as f_dig:
    lst_dig = input("Введите числа через пробел: ").split()
    for el in range(len(lst_dig)):
        f_dig.write(lst_dig[el] + "\n")
f_dig.close()
f_sum = 0
with open("dig.txt", encoding='utf-8') as f_dig:
    for line in f_dig:
        f_sum = f_sum + int(line)
    print(f_sum)
f_dig.close()
