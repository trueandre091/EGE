def f(s, k, m):
    if (s + k) >= 44: return m % 2 == 0
    if m == 0: return False
    h = [
        f(s, s + k, m - 1), f(s + k, k, m - 1)
    ]
    return any(h) if m % 2 != 0 else all(h)

print([s for s in range(1, 100) if f(11, s, 1)][0])
print([s for s in range(1, 100) if f(11, s, 2)][0])

a = []
for s in range(1, 50):
    for x in range(1, 50):
        if f(x, s, 3): a.append((abs(x - s), x, s))
a = sorted(a)

print(a[0])


