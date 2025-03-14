def f(s, e, h = 0):
    if s == e:
        return 1
    if s > e + 1:
        return 0
    return f(s * 3, e) + (f(s**2, e, 1) if h == 0 else 0) + f(s + 2, e)

print(f(2, 64))
