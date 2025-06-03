from itertools import *

def f(a, b, c, d):
    return ((not a) and (not b)) or (b == c) or d

for i in product([0, 1], repeat=4):
    table = [
        (i[0], i[1], 1, i[2]),
        (1, 0, i[3], 1),
        (0, 0, 1, 1)
    ]
    if len(set(table)) == 3:
        for p in permutations("abcd"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [0, 0, 0]:
                print(*p)

# cdba
