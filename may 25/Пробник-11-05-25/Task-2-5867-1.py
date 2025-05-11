from itertools import *

def f(x, y, w, z):
    return (w == (z <= x)) and y

for i in product([0, 1], repeat=5):
    table = [
        (i[0], 0, i[1], 0),
        (1, i[2], 1, 1),
        (i[3], i[4], 0, 0)
    ]
    if len(set(table)) == 3:
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [1, 0, 1]:
                print(*p)

# ywzx

