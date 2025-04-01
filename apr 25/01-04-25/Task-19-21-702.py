def f(s, m):
    if 36 <= s <= 85: return m % 2 == 0
    if s > 85: return m % 2 != 0
    if m == 0: return False
    h = [
        f(s + 2, m - 1), f(s * 3, m - 1)
    ]
    return any(h) if m % 2 != 0 else all(h)

print(f(30, 3), f(32, 2))
print(f(8, 5), f(10, 4))
print(f(6, 6))

