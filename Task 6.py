import itertools

def iterator_int(count):
    for el in itertools.count(count):
        print(el)

def iterator_repeater(my_list):
    for el in itertools.cycle(my_list):
        print(el)

iterator_int(1)
iterator_repeater(["I"])