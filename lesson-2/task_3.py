my_list_month = ["зима","зима","весна","весна","весна","лето","лето","лето","осень","осень","осень","зима"]
my_dict_month =  {1: "зима", 2: "зима", 3: "весна", 4: "весна", 5: "весна", 6: "лето", 7: "лето", 8: "лето", 9: "осень", 10: "осень", 11: "осень", 12: "зима"}
print(my_list_month)
month_num = int(input("Введите номер месяца: "))
print("Результат через список: ", my_list_month[month_num-1])
print("Результат через словарь: ", my_dict_month.get(month_num))
