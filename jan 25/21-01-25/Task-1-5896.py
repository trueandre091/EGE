from itertools import permutations

graph = "АВ ВГ ГД ДБ БЖ ЖА ЗА ЗВ ЗГ ЗД ЖД".split()
mat = "256 135 2457 37 1236 157 346".split()

print(*range(1, 8))

for i in permutations("АБВГДЖЗ"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# В Г Д Б З А Ж
