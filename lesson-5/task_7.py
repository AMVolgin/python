#Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
#строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.

import sys
import json
average_profit = 0
filename = 'firms.txt'
dict1 = {}
dict3 = {}
fields = ['name', 'class', 'prihod', 'rashod', 'profit']
fielsd2 = ['average_profit']

with open(filename, "r", encoding='utf-8') as f_firms:
    l = 1
    for line in f_firms:
         description = list(line.strip().split(None, 3))
         firm_profit = int(description[-2]) - int(description[-1])
         description.append(firm_profit)
         print(description)
         if firm_profit > 0:
             average_profit = average_profit + firm_profit
         sno = 'firms_' + str(l)
         i = 0
         dict2 = {}
         while i < len(fields):
            dict2[fields[i]] = description[i]
            i = i + 1
            dict1[sno] = dict2
         l = l + 1
    out_file = open("firms.json", "w")
    json.dump(dict1, out_file, indent=3)
print(average_profit)
out_file.close()
f_firms.close()



