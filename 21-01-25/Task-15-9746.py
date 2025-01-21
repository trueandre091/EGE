def f(x, y, A):
    return (x < A) or (y < A) or ((x + 2 * y) > 50)

for A in range(1, 1000):
    if all(f(x, y, A) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
        break