def f(x, end):
    if x == 24:
        return 0
    if x == end:
        return 1
    if x < end:
        return 0
    return f(x - 1, end) + f(x - 6, end) + f(x // 2, end)

print(f(34, 29) * f(29, 19) * f(19, 6))

# 115
