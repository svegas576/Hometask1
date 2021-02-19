sal = []

with open("wages.txt", encoding='utf-8') as f:
    data = f.readlines()
    for line in data:
        words = line.split()
        sal.append(int(words[1]))
        if int(words[1]) < 20000:
            print(words[0])

mean = sum(sal) / len(sal)
print(f"Среднее арифметическое зарплат: {mean}")
