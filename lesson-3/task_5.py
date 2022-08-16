def get_sum(my_sum=0):
    # 1 2 3 - ['1',...]
    lst = input("Введите числа через пробел: ").split()
    print(lst)
    for el in range(len(lst)):
        if lst[0] == "$":
            exit("Выход")
            break
        if lst[-1] == "$":
            del lst[-1]
            print(lst)
            my_sum = my_sum + int(lst[el])
        if lst[el] != "q":
            my_sum = my_sum + int(lst[el])
        else:
            break
    print(my_sum)
    if "q" in lst:
        exit("Выход из программы")
    else:
        get_sum(my_sum)

get_sum()
