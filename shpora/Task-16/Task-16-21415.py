from sys import *

setrecursionlimit(10**5)

def f(n):
    if n <= 5: return 1
    return n + f(n - 2)

print(f(2126) - f(2122))

