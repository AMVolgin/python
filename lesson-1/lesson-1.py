print("П1")
a = 10
b = "hello"
print(a)
print(b)
print("П2")
name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
print("Ваше имя: ", name)
print("Ваш возоаст: ", age)
print("П3")
enter_dig = int(input("Введите целое число: "))
result = enter_dig + enter_dig*enter_dig + enter_dig*enter_dig*enter_dig
print("Результат: ", result)
print("П5,П6")
viruch = int(input("Введите размер выручки: "))
rashod = int(input("Ведите размер издержек: "))
if(viruch > rashod):
    print("Фирма приносит доход")
    pribil = viruch - rashod
    rentab = pribil / viruch
    team = int(input("Введите кол-во сотрудников: "))
    for_one = rentab / team
    print("Прибыль на одного:", for_one)
else:
    print("Фирма работает в убыток")
print("П7")
first_day = int(input("Первый день: "))
second_day = int(input("Второй день: "))
count = 0
while first_day <= second_day:
    delta = first_day + (first_day / 100 * 10)
    first_day = first_day + delta
    count = count + 1
print(first_day)



