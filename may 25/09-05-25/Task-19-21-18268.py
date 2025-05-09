from math import *

def f(s, k, m):
    if s + k <= 72:
        return m % 2 == 0
    if m == 0: return False
    h = [
        f(s - 3, k, m - 1),
        f(s, k - 3, m - 1),
        f(ceil(s / 2), k, m- 1),
        f(s, ceil(k / 2), m - 1)
    ]
    return any(h) if m % 2 != 0 else all(h)

print([s for s in range(23, 1000) if f(s, 50, 2)]) # 94
print([s for s in range(23, 1000) if not f(s, 50, 1) and f(s, 50, 3)]) # 51 100
print([s for s in range(23, 1000) if not f(s, 50, 2) and f(s, 50, 4)]) # 103


