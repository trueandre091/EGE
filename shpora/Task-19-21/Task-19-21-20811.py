def f(s, m):
    if s >= 51: return m % 2 == 0
    if m == 0: return False
    h = [
        f(s + 1, m - 1),
        f(s + 4, m - 1),
        f(s * 2 , m -1)
    ]
    return any(h) if m % 2 != 0 else all(h)

print([s for s in range(1, 51) if f(s, 2)])
print([s for s in range(1, 51) if not f(s, 1) and f(s,3)])
print([s for s in range(1, 51) if not f(s, 2) and f(s,4)])

