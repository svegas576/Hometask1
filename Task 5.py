f = open('file.txt', 'w+')
nums = input("Dведите числа через пробелы: ")
f.write(nums)
with open("file.txt", "r+") as f:
    data = f.read().split(' ')
    a = list(data)
    b = map(int,a)
    print("Сумма чисел равна: ", sum(b))
    f.close()



