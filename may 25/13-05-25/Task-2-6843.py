from itertools import *

def f(x, y, w, z):
    return (z <= w) and y and (not x)

for i in product([0, 1], repeat=5):
    table = [
        (0, 1, i[0], 0),
        (i[1], 0, i[2], i[3]),
        (0, 1, 1, i[4])
    ]
    if len(set(table)) == 3:
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [1, 1, 0]:
                print(*p)

# zwyx
