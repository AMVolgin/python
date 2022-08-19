class Road:
    _length = 20
    _width = 5000
    def calc(self):
        s = input("Введите массу асфальта для покрытия одного мерта (кг): ")
        t = input("Введите толщину покрытия (см): ")
        bitum_calc = Road._length * Road._width * int(s) * int(t)
        print("Результат (т): ", bitum_calc/1000)
r = Road()
r.calc()

