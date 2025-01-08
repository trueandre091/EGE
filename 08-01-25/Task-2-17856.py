print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = ((w <= y) <= x) or (not z)
                if not f:
                    print(x, y, w, z)

# z y w x
# 1 1 1 0
# 1 0 0 0
# 1 1 0 0

