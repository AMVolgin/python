class Car():
    speed = 20
    color = "RED"
    name = "KALINA"
    is_police = False
    def go(self):
        print("car go!")
    def stop(self):
        print("car stop!")
    def turn(self, direction):
        print("car go" + direction)
    def show_speed(self, speed):
        if int(speed) > 20:
            print("Car speeding!!!")
        else:
            print("Car normal speeding!!!")

class TownCar(Car):
    def t_go(self):
        print("car go!")
    def show_speed(self, speed):
        if int(speed) > 60:
            print("TownCar speeding!!!")
        else:
            print("TownCar normal speeding!!!")
class SportCar(Car):
    def s_stop(self):
        print("car stop!")
class WorkCar(Car):
    def w_car(self, direction):
        if direction == "r":
            print("car go right")
        else:
            print("car go left")
    def show_speed(self, speed):
        if int(speed) > 40:
            print("WorkCar speeding!!!")
        else:
            print("WorkCar normal speeding!!!")
class PoliceCar(Car):
    def p_police(self, is_police):
        if is_police is True:
            print("car criminal!")
        else:
            print("car not criminal!")

tmp_speed = input("Enter speed: ")
c = Car()
c.show_speed(tmp_speed)
t = TownCar()
t.t_go()
t.show_speed(tmp_speed)
s = SportCar()
s.s_stop()
w = WorkCar()
tmp_direction = input("Enter direction r or l: ")
w.w_car(tmp_direction)
w.show_speed(tmp_speed)
p = PoliceCar()
p.p_police(True)
