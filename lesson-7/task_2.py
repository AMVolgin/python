class Clothes:
    name = ""

class Coat(Clothes):
    def __init__(self, V):
        self.name = "coat"
        self.V = ""

    def size_cloth(self, V):
        size_cloth = round(((int(V) / 6.5) + 0.5), 2)
        print(f"Для пальто нужно {size_cloth} материала")
        return  size_cloth

class Suit(Clothes):
    def __init__(self, H):
        self.name = "suit"
        self.H = ""

    def sizeSuit(self, H):
        size_suit = round((2 * int(H) + 0.3), 2)
        print(f"Для пальто нужно {size_suit} материала")
        return size_suit

class AllCloth(Coat, Suit):
    def summary_cloth(self, ssize_suit, ssize_cloth):
        summary = round(int(ssize_suit) + int(ssize_cloth), 2)
        print(f"Ткани на одежду: {summary}")

cc = Coat("V")
tmp_v = input(f"Введите рост для пальто: {cc.V}")
tmp_cloth = cc.size_cloth(tmp_v)
ss = Suit("H")
tmp_h = input(f"Введите размер для костюма: {ss.H}")
tmp_suit = ss.sizeSuit(tmp_h)
ac = AllCloth("ALL CLOTH")
ac.summary_cloth(tmp_suit, tmp_cloth)


