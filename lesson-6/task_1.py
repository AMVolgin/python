import time
class TrafficLight:
    color = "RED"
    def running(self):
        print("Current color - ", TrafficLight.color)
        time.sleep(7)
        TrafficLight.color = "YELLOW"
        print("Current color - ", TrafficLight.color)
        time.sleep(2)
        TrafficLight.color = "GREEN"
        print("Current color - ", TrafficLight.color)
        time.sleep(5)
c = TrafficLight()
c.running()


