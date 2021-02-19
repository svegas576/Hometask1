words = [input("Введите Ваше имя и фамилию: "), input("Введите Ваш возраст: ")]
with open(r"task1.txt", "w") as f:
    for word  in words:
        f.write(word + '\n')
print()
f.close()
