def func(time,rate,award):
    return time * rate + award
time = int(input("Введите время выработки(час.): "))
rate = int(input("Введите ставку в час (руб.): "))
award = int(input("Введите сумму премии(руб.): "))
print ("Заработная плата сотрудлника равна: ", func(time,rate,award))