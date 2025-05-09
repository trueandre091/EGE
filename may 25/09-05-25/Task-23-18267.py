def f(s, e, l):
    if s == e and l != 2: return 1
    if s > e: return 0
    return f(s + 2, e, 0) + f(s + 5, e, 1) + f(s**2, e, 2)

print(f(4, 36, -1))
# 319
