from itertools import permutations

graph = "AH HC CF FG GH BG BD DE EB EA".split()
matrix = "38 58 146 36 27 347 568 127".split()

print(*range(1, 9))

for i in permutations("ABCDEFGH"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# 6 + 31 = 37
