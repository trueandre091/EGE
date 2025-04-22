from itertools import *

def f(x, y, w, z):
    return (w <= (y == z)) and (y == (z <= x))

for i in product([0, 1], repeat=2):
    table = [
        (i[0], 0, 0, 0),
        (0, i[1], 1, 1),
        (0, 0, 0, 1)
    ]
    if len(set(table)) == 3:
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [1, 1, 0]:
                print(*p)



