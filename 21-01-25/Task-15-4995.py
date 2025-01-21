def dell(n, m):
    return n % m == 0


def f(A):
    for x in range(1, 1000):
        f = (dell(x, 2) <= (not dell(x, 3))) or (x + A >= 80)
        if not f:
            return False
    return True


for A in range(1, 1000):
    if f(A):
        print(A)
        break




