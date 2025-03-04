from sys import setrecursionlimit

setrecursionlimit(10**6)

def f(x):
    if x < 5:
        return 4
    if x > 4:
        return 4 * f(x - 4)

print(f(4444)/f(4400))