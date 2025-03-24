
def f(s, e):
    if s == e:
        return 1
    if s > e:
        return 0
    return f(s + 2, e) + f(s + 5, e) + f(s * 2, e)


print(f(9, 23)*f(23,35) + f(14, 23)*f(23, 35))


