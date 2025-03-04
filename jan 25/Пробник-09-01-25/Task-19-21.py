
def f(a, b, m):
    if a + b >= 131:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [
        f(a + 2, b, m - 1),
        f(a, b + 2, m - 1),
        f(a * 2, b, m - 1),
        f(a, b * 2, m - 1)
    ]
    return any(h) if m % 2 != 0 else all(h)

print(min(s for s in range(1, 123) if f(11, s, 2)))
print(*[s for s in range(1, 123) if not f(11, s, 1) and f(11, s, 3)][:2])
print(min(s for s in range(1, 123) if (f(11, s, 2) or f(11, s, 4)) and not f(11, s, 2)))
