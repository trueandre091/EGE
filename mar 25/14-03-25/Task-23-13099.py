def f(s, e, h = 0):
    if s == e:
        return 1
    if s > e + 1:
        return 0
    return f(s * 2, e) + f(s * 3, e) + (f(s - 1, e, 1) if h == 0 else 0)

print(f(3, 15))




