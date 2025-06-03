from itertools import *

graph = "АБ БГ ГЕ ЕЗ ЗД ДВ ВА ВБ ГД".split()
mat = "67 567 456 35 234 123 12".split()

print(*range(1, 8))

for i in permutations("АБВГДЕЗ"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# Е Д Б А В Г З
# 12 + 9 = 21


