l = ['один', 'два', 'три', 'четыре', 'пять']
l2 = []
f1 = open('numbers.txt',encoding='utf-8')
a = f1.readlines()
e = len(a)
j = 0
for i in a:
    b = i
    c = i.find(' ')
    r = b.replace(i[:c], l[j])
    j = j + 1
    l2.append(r)
    f2 = open('new_numbers.txt', 'w', encoding='utf-8')
    f2.writelines(l2)