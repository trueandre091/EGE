from itertools import *

graph = "BD DE EA AC CG GB GF FE CF".split()
mat = "26 147 456 237 37 13 245".split()

print(*range(1, 8))

for i in permutations("ABCDEFG"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# B G E F A D C
# 39 + 21 = 60
