def f(x, A):
    return (not (x & 79 == 0)) and ((x & 31 == 0) <= (not (x & A == 0)))

for A in range(10000):
    if all(f(x, A) for x in range(90, 101)):
        print(A)
        break