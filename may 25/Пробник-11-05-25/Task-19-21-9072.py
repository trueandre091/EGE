def f(s, m):
    if s >= 100:
        return m % 2 == 0
    if m == 0:
        return False
    h = [
        f(s + 7, m - 1),
        f(s * 2, m - 1),
    ]
    return any(h) if m % 2 != 0 else all(h)

print([s for s in range(1, 100) if f(s, 1)])
print([s for s in range(1, 100) if not f(s, 3) and f(s, 2)])
print([s for s in range(1, 100) if not f(s, 2) and f(s, 4)])


