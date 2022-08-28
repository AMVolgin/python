class Cell:
    number_of_cells = 0

    def __add__(self, jail1, jail2):
        self.number_of_cells = int(jail1) + int(jail2)
        return self.number_of_cells

    def __sub__(self, jail1, jail2):
        self.number_of_cells = int(jail1) - int(jail2)
        if self.number_of_cells < 0:
            print("Коллечество ячеек не может быть меньше 0!")
        return self.number_of_cells
    def __mul__(self, jail1, jail2):
        self.number_of_cells = int(jail1) * int(jail2)
        return self.number_of_cells
    def __truediv__(self, jail1, jail2):
        self.number_of_cells = int(jail1) // int(jail2)
        return self.number_of_cells


cc = Cell()
jj1 = input(f"Введите количество ячеек в первой клетке:")
jj2 = input(f"Введите количество ячеек во второй клетке:")
cc_m = cc.__add__(jj1, jj2)
print(f"Всего ячеек в клетках сложение: {cc_m}")
cc_s = cc.__sub__(jj1, jj2)
print(f"Всего ячеек в клетках вычитание: {cc_s}")
cc_t_d = cc.__sub__(jj1, jj2)
print(f"Всего ячеек в клетках деление: {cc_t_d}")






