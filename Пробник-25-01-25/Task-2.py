# 1 способ
print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (w and y) or ((x <= w) == (y <= z))
                if not f:
                    print(x, y, w, z)

# x y w z
# 1 0 0 0
# 1 0 0 1
# 1 1 0 1

# z w y x
# 0 0 0 1
# 1 0 0 1
# 1 0 1 1


# 2 способ
from itertools import permutations, product

def f(x, y, w, z):
    return (w and y) or ((x <= w) == (y <= z))

for i in product([0, 1], repeat=6):
    table = [
        (i[0], i[1], i[2], 1),
        (1, i[3], i[4], 1),
        (1, i[5], 1, 1)
    ]
    if len(set(table)) == 3:
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [0, 0, 0]:
                print(*p)












