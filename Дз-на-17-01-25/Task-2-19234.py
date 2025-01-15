# 1 способ
from itertools import product, permutations

def f(x, y, w, z):
    return (not (((not x) or y) and (not w))) or (not (z and (not (y and w))))

for i in product([0, 1], repeat=7):
    table = [
        (0, i[0], i[1], 1),
        (i[2], 1, i[3], i[4]),
        (1, 0, i[5], i[6])
    ]
    if len(set(table)) == 3:
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [0, 0, 0]:
                print(*p)

# yxwz

# 2 способ
print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (not (((not x) or y) and (not w))) or (not (z and (not (y and w))))
                if not f:
                    print(x, y, w, z)

# x y w z
# 0 0 0 1
# 0 1 0 1
# 1 1 0 1

# y x w z
# 0 0 0 1
# 1 1 0 1
# 1 0 0 1

# yxwz
