print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = y and (x or z) or (not (y or z)) or w
                if not f:
                    print(x, y, w, z)

# x y w z
# 1 0 0 1
# 0 1 0 0
# 0 0 0 1