def division(first_obj, second_obj):
    try:
        return first_obj/second_obj
    except ZeroDivisionError:
        return "Пытаетесь делить на 0!"

try:
    first_numb = int(input("Введите первое число: "))
    second_numb = int(input("Введите второе число: "))
    print(division(first_numb, second_numb))
except ValueError:
    print("Пожалуйста, вводите только числа")

first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
division(first, second)