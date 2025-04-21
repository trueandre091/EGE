from itertools import *

graph = "AE EG GF FB BA AC CE BD DF CD".split()
mat = "235 146 145 236 137 247 56".split()

print(*range(1, 8))

for i in permutations("ABCDEFG"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# C D A B E F G

