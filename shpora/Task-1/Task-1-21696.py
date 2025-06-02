from itertools import *

graph = "EH HG GC CF FA AE DE DB BH BG DF".split()
mat = "23 168 158 578 347 27 456 234".split()

print(*range(1, 9))

for i in permutations("ABCDEFGH"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7 8
# A F E B H C G D
# 14 + 17 = 31
