def division():
    a = int(input("ведите первое число: "))
    b = int(input("Введите второе число: "))
    if b == 0:
        print("Деление на 0 невозможно!")
    else:
        print(f"Результат деления равен: ", a / b)

division()