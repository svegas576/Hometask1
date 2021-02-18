import functools
def mult(a,b):
    return a * b
gen = [el for el in range(1,11) if el % 2 == 0]
print(functools.reduce(mult, gen))
