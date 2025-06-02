from itertools import *

def f(x, y, w, z):
    return x and (z <= w) and (not y)


for i in product([0, 1], repeat=7):
    table = [
        (i[0], i[1], 1, i[2]),
        (i[3], 1, 0, i[4]),
        (1, 0, i[5], i[6])
    ]
    if len(set(table)) == 3:
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [1, 1, 1]:
                print(*p)

# xwzy
