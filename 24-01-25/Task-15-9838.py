
def f(x, y, A):
    return ((x + 2 * y) > A) or (y < x) or (x < 30)

for A in range(1000):
    if all(f(x, y, A) for x in range(1000) for y in range(1000)):
        print(A)

