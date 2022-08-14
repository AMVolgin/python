print("П7")
first_day = int(input("Первый день: "))
second_day = int(input("Второй день: "))
count = 0
while first_day <= second_day:
    delta = first_day + (first_day / 100 * 10)
    first_day = first_day + delta
    count = count + 1
print(first_day)