def f(x, y):
    return (y > 10) or ((x * A) > (y + x))


for A in range(1, 1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
        break