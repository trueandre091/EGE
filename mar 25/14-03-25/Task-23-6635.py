
def f(s, h):
    if s < 0 and h == 13:
        return [s]
    if h > 13:
        return []
    return f(s * (-3), h + 1) + f(s - 3, h + 1)

print(len(set(f(333, 0))))

