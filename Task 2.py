class Myerror(Exception):
    def __init__(self, num):
        self.num = num

a = int(input("Введите 1-е число: "))
b = int(input("Введите 2-е число: "))

try:
    if b == 0:
        raise Myerror("Деление на 0 невозможно!")
except Myerror as e:
    print(e)
else:
    print(f"Результат равен: {a//b}")