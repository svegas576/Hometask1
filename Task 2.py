from abc import ABC, abstractmethod
class Clothes:

    def __init__(self,name):
        self.name = name
    @property
    @abstractmethod
    def fabrics(self):
        pass

class Coat():
    def __init__(self,name,size):
        self.name = name
        self.size = size
    @property
    def fabrics(self):
        return round(self.size / 6.5 + 0.5)

class Suit():
    def __init__(self,name,height):
        self.name = name
        self.height = height
    @property
    def fabrics(self):
        return round((2 * self.height + 0.3)/100)

suit = Suit("костюм", 140)
coat = Coat("пальто", 46)
print(f'{suit.fabrics}м ткани понадобится для изготовления {suit.name}а')
print(f'{coat.fabrics}м ткани понадобится для изготовления {coat.name}')