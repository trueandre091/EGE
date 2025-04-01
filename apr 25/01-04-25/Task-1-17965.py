from itertools import permutations

graph = "BH HF FD DC CE EA AB AH GE GF GC".split()
mat = "247 148 578 126 38 47 136 235".split()

print(*range(1, 9))

for i in permutations("ABCDEFGH"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7 8
# G E H C B D F A
# 2 + 74 = 76

