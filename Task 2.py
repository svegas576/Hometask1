with open("Pushkin.txt", "r", encoding='utf-8') as f:
    data = f.readlines()
lines = len(data)
i = 1
for j in data:
    words = len(j.split())
    print(f"В {i} строке {words} слов(о/а)")
    i = i + 1
print(f"{lines} строк(а/и)")
f.close()


