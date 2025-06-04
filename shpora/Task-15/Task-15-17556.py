from itertools import *

def f(x):
    B = 70 <= x <= 90
    return (x % A == 0) or (B <= (not (x % 22 == 0)))


for A in range(1, 1000):
    if all(f(x) for x in range(1000)):
        print(A)


