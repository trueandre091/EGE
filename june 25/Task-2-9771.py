from itertools import *

def f(x, y, w, z):
    return (y <= x) and (not z) and w

for i in product([0, 1], repeat=6):
    table = [
        (1, 0, i[0], i[1]),
        (1, 1, i[2], i[3]),
        (i[4], 1, 1, i[5])
    ]
    if len(set(table)) == 3:
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [1, 1, 1]:
                print(*p)

# wxyz
