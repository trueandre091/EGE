def f(s, e, h=""):
    if s == e: return 1
    if s > e + 1: return 0
    return (f(s - 1, e, "A") if h != "A" else 0) + f(s*2, e) + f(s*3, e)

print(f(3, 15))
