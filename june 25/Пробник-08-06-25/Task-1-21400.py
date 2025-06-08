from itertools import *

graph = "EF FA AB BG GE EC CD DF DA".split()
mat = "457 567 45 136 123 247 126".split()

print(*range(1, 8))

for i in permutations("ABCDEFG"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# C A G E B F D
# 18 + 4 = 22
