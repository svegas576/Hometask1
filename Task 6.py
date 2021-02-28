def int_func(word):
    result = ""
    for a in word:
        a = a[0].upper() + a[1:]
        result = result + a + " "
    return result

str1 = input("Введите слова разделенными пробелами ")
print(int_func(str1.split()))