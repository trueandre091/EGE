from itertools import product, permutations

def f(x, y, w, z):
    return (x <= (z == w)) or (not (y <= w))

for i in product([0, 1], repeat=7):
    table = [
        (i[0], 1, i[1], i[2]),
        (0, i[3], 0, i[4]),
        (i[5], 0, 0, i[6])
    ]
    if len(set(table)) == len(table):
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [0, 0, 0]:
                print(*p)

# zwyx

