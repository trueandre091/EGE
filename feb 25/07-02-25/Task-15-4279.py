from itertools import combinations

def f(x):
    return (x & 1097 == 0) <= ((x & 2047 != 0) <= (x & A != 0))

for A in range(1, 10000):
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break

