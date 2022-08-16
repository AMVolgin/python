
def my_func(a1, a2):
    try:
        if int(a1)>0 and int(a2)>0:
            res = a1 ** a2
            print("Результат: ", res)
        if a2 == 0:
            print("Результат: 1")
        if a2<0:
            res = 1/(int(a1) ** int(abs(a2)))
            print("Результат: ", res)
    except ValueError:
        print("Вводите только цифры")


arg1 = input("arg1: ")
arg2 = input("arg2: ")
my_func(arg1,arg2)