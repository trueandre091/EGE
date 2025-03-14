def f(s, e, c=0):
    if s == e and c <= 15:
        return 1
    if s > e:
        return 0
    return f(s + 2, e, c + (1 if (s + 2) % 2 == 0 else 0)) \
            + f(s + 3, e, c + (1 if (s + 3) % 2 == 0 else 0)) \
            + f(s * 2 + 1, e, c + (1 if (s * 2 + 1) % 2 == 0 else 0))

print(f(1, 55))