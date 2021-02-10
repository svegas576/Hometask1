print("___________Товары_______________")
dict2 = []
i = 0
for i in range(0, 3):
    i = i + 1
    name = input("Введите название товара: ")
    price = input("Введите цену товара: ")
    number = input("Введите количество товара: ")
    a = input("Введите единицу измерения: ")
    dict1 = (
    i,{"Название:": [name],
        "Цена:": [price],
        "Количество:": [number],
        "Единица измерения:": [a]})
    dict2.append(dict1)
print(dict2)