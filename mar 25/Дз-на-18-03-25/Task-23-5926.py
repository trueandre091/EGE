a = set()
def f(s, l, h):
    if h == 24:
        a.add(s)
    if h > 24:
        return
    if l == 0:
        f(s + 7, 1, h + 1)
        f(s * 4, 2, h + 1)
    elif l == 1:
        f(s + 1, 0, h + 1)
        f(s * 4, 2, h + 1)
    elif l == 2:
        f(s + 1, 0, h + 1)
        f(s + 7, 1, h + 1)
    else:
        f(s + 1, 0, h + 1)
        f(s + 7, 1, h + 1)
        f(s * 4, 2, h + 1)

f(1, -1, 0)
print(len(a))



