class Stationery:
    def __init__(self,title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")
class Pen(Stationery):
    def __init__(self,title):
        Stationery.__init__(self,title)
    def draw(self):
        print(f"Рисуем ручкой {self.title}")
class Pencil(Stationery):
    def __init__(self,title):
        Stationery.__init__(self,title)
    def draw(self):
        print(f"Рисуем карандашом {self.title}")
class Handle(Stationery):
    def __init__(self,title):
        Stationery.__init__(self,title)
    def draw(self):
        print(f"Рисуем маркером {self.title}")
pen1 = Pen("Parker")
pen1.draw()
pencil1 = Pencil("Kohinoor")
pencil1.draw()
handle1 = Handle("Touch Raven")
handle1.draw()

