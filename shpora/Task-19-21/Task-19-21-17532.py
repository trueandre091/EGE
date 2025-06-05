def f(s, k, m):
    if (s + k) >= 65: return m % 2 == 0
    if m == 0: return False
    h = [
        f(s + 1, k, m - 1), f(s, k + 1, m - 1),
        f(s * 3, k, m - 1), f(s, k * 3, m - 1)
    ]
    return any(h) if m % 2 != 0 else all(h)

print([s for s in range(1, 59) if f(s, 6,2)]) # 7
print([s for s in range(1, 59) if not f(s, 6,1) and f(s, 6, 3)])
print([s for s in range(1, 59) if not f(s, 6,2) and f(s, 6, 4)])

