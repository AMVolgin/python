#Сформировать словарь, содержащий название предмета и общее количество занятий по
#нему. Вывести его на экран
import os
import json
filename = 'predmet.txt'
dict1 = {}
fields = ['predmet', 'lections', 'practics', 'labs']

with open(filename, "r", encoding='utf-8') as fh:
    l = 1
    for line in fh:
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
            out_file = open("predmet.json", "w")
            json.dump(dict1, out_file, indent=3)
            out_file.close()
