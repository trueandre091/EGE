print("x y w z u")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                for u in range(2):
                    f = ((z <= w) and (y == (not x))) <= (u == (y or z))
                    if not f:
                        print(x, y, w, z, u)


# x y w z u
# 0 1 0 0 0

# 0 1 1 0 0
# 1 0 0 0 1

# 0 1 1 1 0
# 1 0 1 0 1
# 1 0 1 1 0

# u y w z x
# 0 1 0 0 0
# 0 1 1 0 0
# 1 0 0 0 1
# 0 0 1 1 1

from itertools import product, permutations

def f(x, y, w, z, u):
    return ((z <= w) and (y == (not x))) <= (u == (y or z))

for i in product([0, 1], repeat=8):
    table = [
        (0, i[0], 0, 0, 0),
        (0, i[1], i[2], 0, 0),
        (i[3], 0, 0, 0, i[4]),
        (0, 0, i[5], i[6], i[7])
    ]
    if len(set(table)) == 4:
        for p in permutations("xywzu"):
            u = [f(**dict(zip(p, j))) for j in table]
            if u == [0, 0, 0, 0]:
                print(*p)