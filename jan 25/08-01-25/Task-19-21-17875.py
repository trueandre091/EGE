import math

def f(s, m):
    if s <= 19:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s - 2, m - 1), f(s // 3, m - 1), f(s - 5, m - 1)]
    return any(h) if m % 2 != 0 else all(h)

print(min([s for s in range(20, 10000) if not f(s, 1)]))
print(*[s for s in range(20, 1000) if not f(s, 1) and f(s, 3)][:2])
print(min([s for s in range(20, 1000) if (f(s, 2) or f(s, 4)) and not f(s, 2)]))

# 60
# 62 63
# 64