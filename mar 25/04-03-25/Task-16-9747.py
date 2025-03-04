from sys import setrecursionlimit

setrecursionlimit(10**6)
def f(n):
    if n < 11: return n
    return n + f(n - 1)

print(f(2024) - f(2021))
