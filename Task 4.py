a = input("Введите несколько слов с пробелами: ").split()   #задача номер 4
for i in range(len(a)):
    if len(list(a)[i]) <= 10:
        print(i+1, list(a)[i])
    else:
            print(i+1, str(list(a)[i])[0:10])


