#Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
#строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.

import sys
import json

filename = 'firms.txt'
dict1 = {}
fields = ['predmet', 'lections', 'practics', 'labs']

with open(filename, "r", encoding='utf-8') as f_firms:
    l = 1
    for line in f_firms:
         description = list(line.strip().split(None, 3))
         print(description)
         sno = 'Predmet' + str(l)
         i = 0
         dict2 = {}
         while i < len(fields):
            dict2[fields[i]] = description[i]
            i = i + 1
            dict1[sno] = dict2
            l = l + 1
            out_file = open("firms.txt.json", "w")
            json.dump(dict1, out_file, indent=3)
            out_file.close()
f_firms.close()


