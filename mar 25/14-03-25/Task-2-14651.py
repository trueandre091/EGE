from itertools import product, permutations

def f(x, y, w, z):
    return ((z <= x) == ((w <= y) or (x and w)))


for i in product([0, 1], repeat=6):
    table = [
        (i[0], i[1], i[2], 1),
        (i[3], i[4], 1, 1),
        (i[5], 1, 1, 1)
    ]
    if len(set(table)) == 3:
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [0, 0, 0]:
                print(*p)













