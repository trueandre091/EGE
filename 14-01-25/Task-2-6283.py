from itertools import product, permutations

def f(x, w, z, y):
    return (not ((not (x <= (not w))) and z)) and (not (w <= z)) and (x <= (not z))

s = set()
for i in product([0, 1], repeat=5):
    table = [
        (1, 0, i[0], 0),
        (1, 0, i[1], i[2]),
        (i[3], 1, i[4], 1)
    ]
    if len(set(table)) == len(table):
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [1, 0, 0]:
                s.add(p)

print(len(s))
