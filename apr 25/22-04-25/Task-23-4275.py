def f(s, e, h = 0):
    if s == e and h <= 3: return 1
    if s > e or h > 3: return 0
    return f(s + 2, e, h) + f(s * 3, e, h + 1) + f(s * 5, e, h + 1)

print(f(2, 200))