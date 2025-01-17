# 1 способ
from itertools import product, permutations

def f(x, y, w, z):
    return ((not x) and (z <= y) and (not w)) or ((z == w) and ((x or y) <= w))

for i in product([0, 1], repeat=4):
    table = [
        (1, 0, 0, 0),
        (i[0], 1, 0, i[1]),
        (1, 0, i[2], i[3])
    ]
    if len(set(table)) == 3:
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [1, 1, 1]:
                print(*p)

# y w x z

# 2 способ
print("x y z w")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = ((not x) and (z <= y) and (not w)) or ((z == w) and ((x or y) <= w))
                if f:
                    print(x, y, w, z)


