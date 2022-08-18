#Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
#строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.

import sys
import json

firm_dict = {}
profit_dict = {}
fields = ['firm_name', 'firm_profit']
res_profit = 0
l = 1
with open("firms.txt", encoding='utf-8') as f_firm:
        for line in f_firm:
            description = list(line.strip().split(None, 3))
            print(description)
            sno = 'firm_' + str(l)


