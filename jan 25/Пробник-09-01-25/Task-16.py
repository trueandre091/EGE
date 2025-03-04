from sys import setrecursionlimit

setrecursionlimit(10**6)

def f(n):
    if n <= 6:
        return n
    return 2 * n + 3 + f(n - 1)

print(f(6188) - f(6185))
