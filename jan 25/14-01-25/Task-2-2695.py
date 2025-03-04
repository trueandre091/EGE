from itertools import product, permutations

def f(x, y, w, z):
    return (w or y) and (x <= (not z)) and (not w)

s = set()
for i in product([0, 1], repeat=5):
    table = [
        (i[0], 0, i[1], 0),
        (1, i[2], i[3], i[4]),
        (1, 1, 0, 0)
    ]
    if len(set(table)) == len(table):
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [1, 1, 1]:
                s.add(p)

print(len(s))

