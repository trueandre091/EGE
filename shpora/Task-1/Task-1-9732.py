from itertools import *

graph = "FB BD DA AG GC CF CE GE BE FE".split()
mat = "47 357 2567 16 236 345 123".split()

print(*range(1, 8))

for i in permutations("ABCDEFG"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# A C E D F B G
# 25