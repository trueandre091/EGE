from itertools import product, permutations

def f(x, y, w, z):
    return x and ((z <= y) == w)

for i in product([0, 1], repeat=5):
    table = [
        (1, i[0], 1, i[1]),
        (0, i[2], 1, 1),
        (1, 1, 1, i[3]),
        (1, 1, 1, i[4])
    ]
    if len(set(table)) == 4:
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [1, 1, 1, 1]:
                print(*p)

