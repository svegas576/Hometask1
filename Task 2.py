def full_name():
    name = str(input("Введите имя: "))
    surname = str(input("Введите фамилию: "))
    birth = str(input("Введите год рождения: "))
    city = str(input("Введите город проживания: "))
    email = str(input("Введите адремс электронной почты: "))
    tel = str(input("Введите номер телефона: "))
    full_name = name + "," + surname + "," + birth + "," + city + "," + email + "," + tel
    print(full_name)


full_name()