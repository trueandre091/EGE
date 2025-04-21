def f(s, k, m):
    if (s + k) <= 100: return m % 2 == 0
    if m == 0: return False
    h = [
        f(s-3, k-3, m-1),
        f(s//2, k, m-1),
        f(s, k//2, m-1)
    ]
    return any(h) if m % 2 != 0 else all(h)

print([s for s in range(53, 1000) if f(s, 48, 2)]) # 59
print([s for s in range(53, 1000) if not f(s, 48, 1) and f(s, 48, 3)])
print([s for s in range(53, 1000) if not f(s, 48, 2) and f(s, 48, 4)])

