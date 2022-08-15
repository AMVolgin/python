my_dig_list = input("Введите числа через пробел: ").split()
print(my_dig_list)
my_dig_list_len = len(my_dig_list)
if(my_dig_list_len%2) == 0:
    print("В списке четное колличество элементов")
    for i in range(0, len(my_dig_list) - 1, 2):
        my_dig_list[i], my_dig_list[i + 1] = my_dig_list[i + 1], my_dig_list[i]
    print(my_dig_list)
else:
    print("В списке не четное колличество элементов")
    for i in range(0, len(my_dig_list) - 2, 2):
        my_dig_list[i], my_dig_list[i + 1] = my_dig_list[i + 1], my_dig_list[i]
    print(my_dig_list)