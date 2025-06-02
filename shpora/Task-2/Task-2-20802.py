from itertools import *

def f(x, y, w, z):
    return (w <= (not (z <= x))) or y

for i in product([0, 1], repeat=7):
    table = [
        (1, i[0], i[1], i[2]),
        (0, 1, 0, i[3]),
        (i[4], 0, i[5], i[6])
    ]
    if len(set(table)) == 3:
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [0, 0, 0]:
                print(*p)

# zxyw
