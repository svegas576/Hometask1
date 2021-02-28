class Road(list):
    def __init__(self,length,width):
        self._length = length
        self._width = width

    def append(self,mass):
        list.append(self,mass)

    def road_mass(self,length,width):
        road_mass = self._length * self._width * 25 * 5
        return road_mass

r = Road(20, 5000)
print(f"Длина дороги -{r._length}, ширина дороги - {r._width}")
r.road_mass(20,5000)
print(f"масса асфальта, необходимого для покрытия всего дорожного полотна, равна: {r.road_mass(30,40)}")