def f(s, k, m):
    if s * k >= 777:
        return m % 2 == 0
    if m == 0:
        return False
    h = [
        f(s + 3, k, m - 1),
        f(s, k + 3, m - 1),
        f(s * 2, k, m - 1),
        f(s, k*2, m - 1)
    ]
    return any(h) if m % 2 != 0 else all(h)

print(min(s for s in range(1, 111) if f(s, 7, 2))) # 28 заменить all на any
print(sorted([s for s in range(1, 111) if not f(s, 7, 1) and f(s, 7, 3)])) # 25 52
print(min(s for s in range(1, 111) if f(s, 7, 4) and not f(s, 7, 2))) # 33
