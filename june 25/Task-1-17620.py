from itertools import permutations

graph = "AB BD DG GC CE EF FA FB ED".split()
mat = "256 1334 267 27 16 135 34".split()

print(*range(1, 8))

for i in permutations("ABCDEFG"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# B D E G A F C
# 53 + 2 = 55
