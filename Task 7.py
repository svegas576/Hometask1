import itertools
import math

def fgen():
    for el in itertools.count(1):
        yield math.factorial(el)
gen = fgen()
b = 0
for a in gen:
    if b < 4:
        print(a)
        b = b + 1
    else:
        break
