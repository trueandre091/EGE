from itertools import permutations

graph = "GF FE ED DA AG BG BA BC CB CD".split()
mat = "26 147 456 236 37 134 25".split()

print(*range(1, 8))

for i in permutations("ABCDEFG"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# C D G A F B E

