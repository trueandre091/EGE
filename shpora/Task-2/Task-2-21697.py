from itertools import *

def f(x, y, w, z):
    return (not (x <= y)) or (z == w) or z

for i in product([0, 1], repeat=7):
    table = [
        (0, 0, i[0], i[1]),
        (i[2], i[3], 1, i[4]),
        (i[5], 1, 0, i[6])
    ]
    if len(set(table)) == 3:
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [0, 0, 0]:
                print(*p)

# zyxw
