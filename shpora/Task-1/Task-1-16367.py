from itertools import *

graph = "AC CD DF FE EB BG GA BA FC".split()
mat = "246 16 57 15 347 127 356".split()

print(*range(1, 8))

for i in permutations("ABCDEFG"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# B G D E F A C
