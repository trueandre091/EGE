
def f(s, e):
    if s == e:
        return 1
    if s < e or s == 36 or s == 100:
        return 0
    if s > e:
        h = [
            f(s//2,e), f(s//3,e), f(s - 3, e)
        ]
        return sum(h)

print(f(163, 45)*f(45, 3))
