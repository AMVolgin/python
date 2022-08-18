#Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
#строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.

import sys
import json

firm_dict = {}
profit_dict = {}
fields = ['firm_name', 'firm_profit']
res_profit = 0
l = 1
tmp_firm_desc = []
with open("firms.txt", encoding='utf-8') as f_firm:
        for line in f_firm:
            description = list(line.strip().split(None, 3))
            tmp_firm_desc.append(description[0])
            tmp_firm_desc.append(int(description[-2]) - int(description[-1]))
            print(tmp_firm_desc)
            sno = 'firm_' + str(l)
            i = 0
            dict2 = {}
            while i < len(fields):
                dict2[fields[i]] = str(tmp_firm_desc[i][0])
                i = i + 1
            firm_dict[sno] = dict2
            l = l + 1
        out_file = open("firms.json", "w")
        json.dump(firm_dict, out_file, indent=3)
        out_file.close()
        f_firm.close()

