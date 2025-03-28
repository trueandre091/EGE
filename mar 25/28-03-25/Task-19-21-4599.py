def f(s, k, m):
    if s >= 259: return m % 2 == 0
    if m == 0: return False
    h = [
        f(s + 1, k, m - 1), f(s, k + 1, m - 1),
        f(s *2, k, m - 1), f(s, k * 2, m - 1)
    ]
    return any(h)

print([s for s in range(1, 242) if f(s, 2)])