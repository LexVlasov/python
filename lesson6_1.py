# задание 1
import time

class TrafficLight:
    def running(self):
        while True:
            print('Красный')
            time.sleep(7)
            print('Желтый')
            time.sleep(2)
            print('Зеленый')
            time.sleep(5)
            print('Желтый')
            time.sleep(2)


svetofor = TrafficLight()
print(svetofor.running())