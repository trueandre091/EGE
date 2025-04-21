def f(s, k, m):
    if (s + k) >= 81: return m % 2 == 0
    if m == 0: return False
    h = [
        f(s+1, k, m-1), f(s, k+1, m-1),
        f(s*2, k, m-1), f(s, k*2, m-1)
    ]
    return any(h) if m % 2 != 0 else all(h)

print([s for s in range(1, 74) if f(s, 7, 2)]) #19
print([s for s in range(1, 74) if not f(s, 7, 1) and f(s, 7, 3)])
print([s for s in range(1, 74) if not f(s, 7, 2) and f(s, 7, 4)])


