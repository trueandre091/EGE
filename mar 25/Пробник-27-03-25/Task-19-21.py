def f(s, k, m):
    if (s + k) >= 127:
        return m % 2 == 0
    if m == 0:
        return False
    h = [
        f(s + 2, k, m - 1), f(s, k + 2, m - 1),
        f(s * 3, k, m - 1), f(s, k * 3, m - 1)
    ]
    return any(h) if m % 2 != 0 else all(h)

# print([s for s in range(1, 123) if f(s, 2, 2)][0])
print([s for s in range(1, 123) if not f(s, 2, 1) and f(s, 2, 3)])
print([s for s in range(1, 123) if not f(s, 2, 2) and f(s, 2, 4)][0])
