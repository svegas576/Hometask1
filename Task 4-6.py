#проект "Склад оргтехники"
class Warehouse:
    def __init__(self):
        self._dict = {}
    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)
    def extract(self, model):
        if self._dict[model]:
            self._dict.setdefault(model).pop(0)

class Equipment(Warehouse):
    def __init__(self,model,number):
        self.model = model
        self.number = number
        self.group = self.__class__.__name__

    def group_name(self):
        return self.group

    def __repr__(self):
        return f'{self.model} {self.number}'

class Printer(Equipment):
    def __init__(self,model,number,type):
        Equipment.__init__(self, model, number)
        self.type = type
        print(f'Модель принтера-{self.model},Количество-{self.number},Тип:{self.type}')

class Scanner(Equipment):
    def __init__(self,model,number,expansion):
        Equipment.__init__(self, model, number)
        self.expansion = expansion
        print(f'Модель сканера-{self.model},Количество-{self.number},Расширение:{self.expansion}')

class Xerox(Equipment):

    def __init__(self, model, number, speed):
        Equipment.__init__(self, model, number)
        self.speed = speed
        print(f'Модель ксерокса-{self.model},Количество-{self.number},Печать:{self.speed}стр/мин ')

warehouse = Warehouse()
s = Scanner("Canon",60,"2400х4800 ")
s1 = Scanner("Canon", 100, "2400x3800")
warehouse.add_to(s)
warehouse.add_to(s1)
x = Xerox("Xerox", 30, 100)
warehouse.add_to(x)
p = Printer('HP',50,'Coloured')
warehouse.add_to(p)
print(warehouse._dict)
