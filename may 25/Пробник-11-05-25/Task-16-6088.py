from sys import setrecursionlimit
setrecursionlimit(10**5)
def f(n):
    if n > 3000: return 1
    if n % 2 == 0:
        return f(n + 1) - n + 1
    else:
        return f(n + 2) - 2 * n + 2

print(2 * f(39) - 2 * f(34))


