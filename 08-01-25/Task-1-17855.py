from itertools import permutations

graph = "EC CG CA AB DB DG DF FG FE".split()
matrix = "457 46 567 12 136 235 13".split()

print(*range(1, 8))

for i in permutations("ABCDEFG"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# DG + AC = 8 + 30 = 38

