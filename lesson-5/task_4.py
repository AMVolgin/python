#Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
#этом английские числительные должны заменяться на русские. Новый блок строк должен
#записываться в новый текстовый файл

import sys
with open("out.txt", "w" ,encoding='utf-8') as f_out:
    with open("in.txt", encoding='utf-8') as f_in:
        for line in f_in:
            lst_in = line.split()
            if lst_in[0] == "One":
                lst_in[0] = "Один"
                f_out.write(str(lst_in) + "\n")
            elif lst_in[0] == "Two":
                lst_in[0] = "Два"
                f_out.write(str(lst_in) + "\n")
            elif lst_in[0] == "Three":
                lst_in[0] = "Три"
                f_out.write(str(lst_in) + "\n")

f_in.close
f_out.close