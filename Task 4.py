class Car:
    def __init__(self,speed,color,name,is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
    def go(self):
        print(f"Машина {self.name} поехала")
    def stop(self):
        print(f"Машина {self.name} остановилась")
    def turn(self,direction):
        print(f"Машина {self.name} повернула {direction}")
    def show_speed(self):
        print(f"Текущая скорость {self.name} равна {self.speed}")
class TownCar(Car):
    def __init__(self,speed,color,name,is_police):
        Car.__init__(self,speed,color,name,is_police)
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name}!Превышение скорости!")
        else:
            print(f"Скорость {self.name} равна {self.speed}")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name}!Превышение скорости!")
        else:
            print(f"Скорость {self.name} равна {self.speed}")
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

audi = TownCar(80,"red","Ауди",False)
ferrari = SportCar(100,"blue","Феррари",False)
kamaz = WorkCar(60,"brown","Камаз",False)
police = PoliceCar(90,"white","полиция",True)

print(audi.speed, audi.color, audi.name, audi.is_police)
print(ferrari.speed, ferrari.color, ferrari.name, ferrari.is_police)
print(kamaz.speed, kamaz.color, kamaz.name, kamaz.is_police)
print(police.speed, police.color, police.name, police.is_police)

ferrari.go()
kamaz.go()
kamaz.show_speed()
audi.go()
audi.show_speed()
police.go()
kamaz.turn("направо")
audi.turn("налево")
audi.stop()
police.stop()
