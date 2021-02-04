input_int = input("Введите целое положительное число: ")
max = 0
while input_int:
    right = input_int % 10
    if right > max:
        max = right
        input_int = input_int // 10
    print(max)