def my_func():
    i = input("Введите числа через пробел: ").split(" ")
    a = 0
    while a < len(i):
        i[a] = int(i[a])
        a = a + 1
    sum = 0
    for c in i:
        sum = sum + c
    print(sum)
my_func()