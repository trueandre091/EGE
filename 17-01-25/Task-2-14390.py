from itertools import product, permutations

def f(x, y, w, z):
    return (z and (not w)) or (z == x) or y

for i in product([0, 1], repeat=4):
    table = [
        (i[0], i[1], 0, 1),
        (1, 0, i[2], 1),
        (1, 1, 0, i[3])
    ]
    if len(set(table)) == 3:
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [0, 0, 0]:
                print(*p)

# w z y x
