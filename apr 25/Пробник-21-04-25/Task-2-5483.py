from itertools import *

def f(x, y, w, z):
    return (z == (not x)) <= ((w <= (not y)) and (y <= x))

for i in product([0, 1], repeat=5):
    table = [
        (1, 1, 1, 0),
        (i[0], i[1], 0, 0),
        (i[2], 0, i[3], i[4])
    ]
    if len(set(table)) == 3:
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [1, 0 ,0 ]:
                print(*p)

