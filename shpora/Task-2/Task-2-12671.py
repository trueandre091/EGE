from itertools import *

def f(x, y, w, z):
    return (not (x == (w and (not z)))) and (y == (x and (not w)))

for i in product([0, 1], repeat=6):
    table = [
        (i[0], i[1], 0, i[2]),
        (i[3], 0, i[4], 0),
        (0, i[5], 1, 0)
    ]
    if len(set(table)) == 3:
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [1, 1, 1]:
                print(*p)

# wxyz
