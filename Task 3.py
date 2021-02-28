def my_func():
    a = int(input("ведите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))
    sum_num = a + b + c - min(a,b,c)
    print(sum_num)

my_func()