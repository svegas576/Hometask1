a = list(input("Ввндите список: "))  # Задача номер 2
n = len(a)
i=0
while i <= n:
    if n % 2 == 0:
        for i in range(0,n,2):
            c = a[i]
            a[i] = a[i + 1]
            a[i + 1] = c
    if n % 2 != 0:
        for i in range(0,n - 1,2):
            c = a[i]
            a[i] = a[i + 1]
            a[i + 1] = c
    break
print(a)































