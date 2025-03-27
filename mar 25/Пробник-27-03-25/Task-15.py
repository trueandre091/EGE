def f(x, y):
    return ((x + 2) <= 50) or (y < (x + 10)) or (x >= A)


for A in range(1, 10000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
