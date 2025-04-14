def f(s, m, last):
    if s > 40: return m % 2 == 0
    if m == 0: return False
    if last == 0:
        h = [f(s + 6, m - 1, 1), f(s * 2, m - 1, 2)]
    elif last == 1:
        h = [f(s + 3, m - 1, 0), f(s * 2, m - 1, 2)]
    elif last == 2:
        h = [f(s + 3, m - 1, 0), f(s + 6, m - 1, 1)]
    else:
        h = [f(s + 3, m - 1, 0), f(s + 6, m - 1, 1), f(s * 2, m - 1, 2)]
    return any(h) if m % 2 != 0 else all(h)

print([s for s in range(2, 37) if not f(s, 1, 3) and f(s, 2, 3)])
print([s for s in range(2, 37) if not f(s, 1, 3) and f(s, 3, 3)])
print([s for s in range(2, 37) if not f(s, 2, 3) and f(s, 4, 3)])





