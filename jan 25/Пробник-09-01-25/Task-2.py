print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (x or (not y)) and (not (x == z)) and w
                if f:
                    print(x, y, w, z)

x y w z
0 0 1 1
1 0 1 0
1 1 1 0

z y x w
1 0 0 1
0 0 1 1
0 1 1 1
