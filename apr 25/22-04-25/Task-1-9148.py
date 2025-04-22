from itertools import *

graph = "АГ ГЖ ЖЗ ЗД ДВ ВА АБ БГ ВБ ДГ ЕЖ ЕД ЕЗ".split()
mat = "256 1458 478 237 126 158 348 2367".split()

print(*range(1, 9))

for i in permutations("АБВГДЕЖЗ"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)





