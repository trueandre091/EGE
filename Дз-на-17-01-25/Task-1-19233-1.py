from itertools import permutations

graph = "DB BC CH HF FA AG GD DB ED EB EH GF".split()
mat = "234 157 147 138 268 58 23 456".split()

print(*range(1, 9))

for i in permutations("ABCDEFGH"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7 8
# E H B D F A C G

# AG + DE = 6-8 + 1-4 = 4 + 7 = 11
