from itertools import permutations, product

def f(x, y, w, z):
    return (not (w <= z)) or (x <= y) or (not x)

for i in product([0, 1], repeat=7):
    table = [
        (1, i[0], i[1], i[2]),
        (0, 1, 0, i[3]),
        (i[4], 0, i[5], i[6])
    ]
    if len(set(table)) == len(table):
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [0, 0, 0]:
                print(*p)

# wzyx
