from itertools import permutations

graph = "BD DE EA AG GF FB CB CE CG".split()
mat = "47 57 45 136 236 457 126".split()

print(*range(1, 8))

for i in permutations("ABCDEFG"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# A D F G B C E
# 13 + 11 + 17 = 41
