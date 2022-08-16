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