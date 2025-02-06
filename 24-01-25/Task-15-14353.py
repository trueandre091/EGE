def tr(a, b, c):
    return max(a, b, c) < sum([a, b, c]) - max(a, b, c)

def f(x, A):
    return tr(A, 7, x) <= ((max(x + 5, 14) <= 27) == (not tr(36, 21, x)))

for A in range(1, 1000):
    if all(f(x, A) for x in range(1, 1000)):
        print(A)

# 50
