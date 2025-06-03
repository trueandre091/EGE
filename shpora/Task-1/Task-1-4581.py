from itertools import *

graph = "AD DE EG GC CF FA AB FB EB".split()
mat = "37 367 125 56 34 247 126".split()

print(*range(1, 8))

for i in permutations("ABCDEFG"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# D B E C G F A
# 13 + 53 = 66

