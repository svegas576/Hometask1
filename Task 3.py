class Cell:
    def __init__(self,number):
        self.number = number

    def __add__(self,other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        sub = self.number - other.number
        if sub > 0:
            return Cell(sub)
        else:
            return "Разность отрицательная!"

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self,other):
        return Cell(self.number // other.number)

    def __str__(self):
        return f"Результат равен: {self.number}"

    def make_order(self, nums):
        print('\n'.join(['*' * nums for i in range(self.number//nums)]) + '\n' + '*' * (self.number % nums))


c1 = Cell(21)
c2 = Cell(30)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
c1.make_order(5)

