def dell(n, m):
    return n % m == 0

def f(x):
    return (dell(x, 10) and dell(x, 26) and (x >= 300)) <= (A <= x)

for A in range(10000):
    if all(f(x) for x in range(1, 1000)):
        print(A)

