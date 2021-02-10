a = int(input("Введите номер месяца: "))
data = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
dict1 = {1: "зима",2: "весна",3: "лето",4: "осень"}
if a in data[0]:
    print("Это ",dict1[1])
elif a in data[1]:
    print("Это ",dict1[2])
elif a in data[2]:
    print("Это ",dict1[3])
elif a in data[3]:
    print("Это ", dict1[4])
else:
    print("Такого месяца не существует!")
