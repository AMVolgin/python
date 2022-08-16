def my_func(a1,a2,a3):
    tmp_list = []
    tmp_list.append(int(a1))
    tmp_list.append(int(a2))
    tmp_list.append(int(a3))
    tmp_list.sort()
    tmp_sum = tmp_list[-1] + tmp_list[-2]
    print(f'After sorting: {tmp_list}')
    print("Сумма наибольших двух аргументов", tmp_sum)


arg1 = int(input("arg1: "))
arg2 = int(input("arg2: "))
arg3 = int(input("arg3: "))
my_func(arg1,arg2,arg3)
