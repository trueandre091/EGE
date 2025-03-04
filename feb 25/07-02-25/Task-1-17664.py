from itertools import permutations

graph = "CH HB BE EA AF FC CG GD DH AB".split()
mat = "248 157 456 136 23 34 28 17".split()

print(*range(1, 9))

for i in permutations("ABCDEFGH"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7 8
# H C A B F E G D

# 21 + 2 = 23
