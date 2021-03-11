from itertools import count
from math import factorial
def fibo_gen():
    for el in count(1):
        yield factorial(el)
gen = fibo_gen()
a = 0
for b in gen:
    if a < 15:
        print(b)
        a += 1
    else:
        break