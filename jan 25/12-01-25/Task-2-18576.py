from itertools import permutations, product

def f(x, y, w, z):
    return not (w <= (x == (y or y))) and (z <= x)

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [
        (a1, 1, 1, a2),
        (0, a3, a4, 0),
        (a5, 0, 1, 0)
    ]
    if len(set(table)) == len(table):
        for p in permutations("xywz"):
            u = [f(**dict(zip(p, t))) for t in table] == [True, True, True]
            if u:
                print(*p)

print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if f(x, y, w, z):
                    print(x, y, w, z)

# x y w z
# 1 0 1 1
# 0 1 1 0
# 1 0 1 0
#
# y x w z
# 0 1 1 1
# 0 1 1 0
# 1 0 1 0
