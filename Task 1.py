list1 = [[3,2,2], [10,8.25], [28,68,119]]
list2 = [[567,75,98],[123,7,9],[10,5,68]]
class Matrix:

    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        return '\n'.join(map(str,self.matr))

    def __add__(self):
        num2 = ()
        for i in range(len(self.matr)):
            num2.append([])
            for j in range(len(self.matr[0])):
                num2(i).append(self.matr[i][j]) + other.matr[i][j]
        return '\n'.join(map(str,num2))
num1 = Matrix(list1)
num3 = Matrix(list2)
print(num1)
print(num3, 7)




