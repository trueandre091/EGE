from itertools import permutations

graph = "АГ ГЖ ЖЗ ЗД ДВ ВА БГ БА БВ ГД ЕЖ ЕЗ ЕД".split()
mat = "256 1458 478 237 126 158 348 2367".split()

print(*range(1, 9))

for i in permutations("АБВГДЕЖЗ"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 5 3 7

