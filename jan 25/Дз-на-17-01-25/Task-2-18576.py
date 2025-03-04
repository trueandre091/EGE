# 1 способ
from itertools import product, permutations

def f(x, y, w, z):
    return (not (w <= (x == (y or y)))) and (z <= x)

for i in product([0, 1], repeat=5):
    table = [
        (i[0], 1, 1, i[1]),
        (0, i[2], i[3], 0),
        (i[4], 0, 1, 0)
    ]
    if len(set(table)) == 3:
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [1, 1, 1]:
                print(*p)

# yxwz

# 2 способ
print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (not (w <= (x == (y or y)))) and (z <= x)
                if f:
                    print(x, y, w, z)

# x y w z
# 1 0 1 1
# 1 0 1 0
# 0 1 1 0

# y z w x
# 0 1 1 1
# 0 0 1 1
# 1 0 1 0

# y x w z
# 0 1 1 1
# 0 1 1 0
# 1 0 1 0

# yxwz
