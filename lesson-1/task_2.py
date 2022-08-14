sec = int(input("Веедите время в секундах"))
sec = sec % (24 * 3600)
hour = sec // 3600
sec %= 3600
min = sec // 60
sec %=60
print("%02d:%02d:%02d" %  (hour, min, sec))