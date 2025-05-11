def f(x, y, w, z):
    return (w == (z <= x)) and y

print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                print(x, y, w, z, int(f(x, y, w, z)))

# x y w z
# 0 1 0 1 1

# 0 1 1 1 0
# 1 0 1 1 0
# 1 1 0 1 0

# 0 1 1 0 1


# y w z x
# 1 0 1 0

# 1 0 1 1

# 1 1 0 0


# ywzx


