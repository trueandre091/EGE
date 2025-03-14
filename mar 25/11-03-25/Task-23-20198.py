from sys import setrecursionlimit

setrecursionlimit(10**6)
def f(s, e, x):
    if s > e:
        return 0
    if s == e:
        return 1
    if x.count("0") >= 2: return 0
    return f(s+5, e, x + "1") + f(s // 2, e, x + "2") + f(s-1, e, x + "0")

print(f(5, 34, ""))