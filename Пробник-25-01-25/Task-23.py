def f(s, e):
    if s > e:
        return 0
    if s == e:
        return 1
    if s < e:
        return f(s + 2, e) + f(s + max(map(int, str(s))), e)

print(f(32, 55) * f(55, 76))