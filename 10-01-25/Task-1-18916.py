from itertools import permutations

graph = "АБ БД ДЖ ЖЗ ЗЕ ЕГ ГВ ВА ВБ ГД ЕЖ".split()
mat = "356 358 128 67 127 147 456 23".split()

print(*range(1, 9))

for i in permutations("АБВГДЕЖЗ"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)
