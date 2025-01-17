from itertools import product, permutations

def f(x, y, z):
    return x <= (y and z)

table = [
    (0, 1, 0),
    (1, 1, 0)
]
for p in permutations("xyz"):
    u = [f(**dict(zip(p, j))) for j in table]
    if u == [0, 0]:
        print(*p)