# 1 способ
print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (x <= (y and (not z))) or w
                if not f:
                    print(x, y, w, z)

# x y w z
# 1 0 0 0
# 1 0 0 1
# 1 1 0 1

# y w x z
# 0 0 1 0
# 0 0 1 1
# 1 0 1 1

# 2 способ
from itertools import product, permutations

def f(x, y, w, z):
    return (x <= (y and (not z))) or w

for i in product([0, 1], repeat=6):
    table = [
        (i[0], i[1], 1, 0),
        (0, i[2], i[3], 1),
        (1, i[4], 1, i[5])
    ]
    if len(set(table)) == 3:
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [0, 0, 0]:
                print(*p)

# ywxz
