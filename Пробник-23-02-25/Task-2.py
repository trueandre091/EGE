def f(x, y, w, z):
    return (not (x == (w and (not z)))) and (y == (x and (not w)))

print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if f(x, y, w, z):
                    print(x, y, w, z)

# x y w z
# 1 1 0 1

# 1 0 1 1
# 0 0 1 0
# 1 1 0 0

# x w y z
# 1 1 0 1
# 0 1 0 0
# 1 0 1 0

# w x y z
# 1 1 0 1
# 1 0 0 0
# 0 1 1 0

print()
##########################
from itertools import product, permutations

for i in product([0, 1], repeat=6):
    table = [
        (i[0], i[1], 0, i[2]),
        (i[3], 0, i[4], 0),
        (0, i[5], 1, 0)
    ]
    if len(set(table)) == 3:
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [1, 1, 1]:
                print(*p)

