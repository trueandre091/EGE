def f(s, e, c=0):
    if s == e and c == 51: return 1
    if s > e: return 0
    return f(s * 4, e, c + 1) + f(s + 1, e, c + 1) + f(s * 3, e, c + 1)





