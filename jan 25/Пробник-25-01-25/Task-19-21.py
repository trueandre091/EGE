from sys import setrecursionlimit

setrecursionlimit(10**6)


def f(a, b, m):
    if a + b >= 300:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [
        f(a+3, b, m - 1),
        f(a, b+3, m - 1),
        f(a*2, b, m - 1),
        f(a, b*2, m - 1)
    ]
    return any(h) if m % 2 != 0 else all(h)

print(min(s for s in range(1, 280) if not f(20, s, 2) and f(20, s, 4)))
