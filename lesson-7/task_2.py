class Clothes:
    name = ""

class Coat(Clothes):
    def __init__(self, V):
        self.name = "coat"
        self.V = ""

    def sizeCloth(self, V):
        size_cloth = round(((int(V) / 6.5) + 0.5), 2)
        return f"Для пальто нужно {size_cloth} материала"

class Suit(Clothes):
    def __init__(self, H):
        self.name = "suit"
        self.H = ""

    def sizeSuit(self, H):
        size_suit = round((int(2*H) + 0.3), 2)
        return f"Для пальто нужно {size_suit} материала"

class MySummary(Coat,Suit):
    def __init__(self):




cc = Coat("V")
tmp_v = input(f"Введите рост для пальто: {cc.V}")
cc.sizeCloth(tmp_v)
ss = Suit("H")
tmp_h = input(f"Введите размер для костюма: {ss.H}")
cc.sizeCloth(tmp_h)

