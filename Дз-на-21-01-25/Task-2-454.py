from itertools import product, permutations

def f(a, b, c, d):
    return ((not (b <= a)) and (c <= d)) or (a and b and c and (not d))

for i in product([0, 1], repeat=9):
    table = [
        (i[0], 0, 0, 0),
        (i[1], i[2], i[3], 0),
        (i[4], i[5], 0, 0),
        (i[6], 0, i[7], i[8])
    ]
    if len(set(table)) == 4:
        for p in permutations("abcd"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [1, 1, 1, 1]:
                print(*p)
# bdca
