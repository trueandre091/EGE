def f(s, k, m):
    if (s + k) >= 175: return m % 2 == 0
    if m == 0: return False
    h = [f(s+1, k, m-1), f(s, k+1, m-1), f(s*3, k, m-1), f(s, k*3, m-1)]
    return any(h) if m % 2 != 0 else all(h)

print([s for s in range(1, 155) if f(s, 19, 2)]) # 4
print([s for s in range(1, 155) if not f(s, 19, 1) and f(s, 19, 3)])
print([s for s in range(1, 155) if not f(s, 19, 2) and f(s, 19, 4)])


