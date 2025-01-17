from itertools import product, permutations

def f1(x, y, w, z):
    return (w == x) and (y <= z)

def f2(x, y, w, z):
    return (w <= x) <= (y == z)

for i in product([0, 1], repeat=4):
    table = [
        (1, i[0], 1, 1),
        (i[1], 1, 0, 0),
        (i[2], 0, 0, i[3])
    ]
    if len(set(table)) == 3:
        for p in permutations("zywx"):
            u = [(f1(**dict(zip(p, x))), f2(**dict(zip(p, x)))) for x in table]
            for f_2 in range(2):
                if u == [(1, 0), (1, f_2), (0, 0)]:
                    print(*p)

