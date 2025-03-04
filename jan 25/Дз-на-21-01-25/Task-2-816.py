from itertools import product, permutations

def f(x, y, z):
    return not (x == (y <= z))

table = [
    (0, 0, 1),
    (0, 1, 1)
]

for p in permutations("xyz"):
    if [f(**dict(zip(p, x))) for x in table] == [1, 0]:
        print(*p)

# yxz

