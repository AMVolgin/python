class Stationery:
    title = "not"
    def draw(self):
        print("To draw not")

class Pen(Stationery):
        def draw_pen(self, title_pen):
            print(f"TO draw: {title_pen}")

class Pencil(Pen):
    def draw_pensil(self, title_pensil):
            print(f"TO draw: {title_pensil}")

class Handle(Pencil):
    def draw_handle(self, title_handle):
        print(f"TO draw: {title_handle}")

pen = Pen()
pen.draw_pen("pen")
pensil = Pencil()
pensil.draw_pensil("pencil")
handle = Handle()
handle.draw_handle("handle")

