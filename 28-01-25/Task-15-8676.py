def f(x):
    return ((x & 500 != 0) and (x & 200 == 0)) <= (not (x & A == 0))

for A in range(10000):
    if all(f(x) for x in range(1000)):
        print(A)
        break