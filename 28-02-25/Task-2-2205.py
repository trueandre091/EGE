from itertools import permutations, product

def f(H, L, W, N):
    return (not (H <= L)) <= ((not (W <= N)) and H)

for i in product([0, 1], repeat=6):
    table = [
        (0, 0, 0, i[0]),
        (0, 0, i[1], i[2]),
        (0, i[3], i[4], i[5])
    ]
    if len(set(table)) == 3:
        for p in permutations("HLWN"):
            u = [f(**dict(zip(p, x))) for x in table]
            if u == [0, 0, 0]:
                print(*p)