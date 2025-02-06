def f(x, y):
    return (x - y >= 39) or (y <= x) or (y >= A - 20)

a = []
for A in range(1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        a.append(A)

print(max(a))

