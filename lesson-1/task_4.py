num = int(input("Введите число: "))
m = 0
for n in str(num):
    if int(n) > m:
        m = int(n)
print("Наибольшая из введенных цифр: ", m)