from itertools import *

def f(x, y, z, w):
    return (not w) and ((y or z) <= ((not x) and y))

for i in product([0, 1], repeat=8):
    table = [
        (i[0], i[1], i[2], 1),
        (i[3], i[4], 1, i[5]),
        (i[6], 1, 1, i[7])
    ]
    if len(set(table)) == 3:
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [1, 1, 1]:
                print(*p)

# wzyx


