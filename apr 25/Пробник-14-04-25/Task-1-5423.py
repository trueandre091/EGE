from itertools import *

graph = "АБ БД ДЕ ЕЗ ЗЖ ЖВ ВГ ГА АД ГД ВЗ".split()
mat = "245 15 478 135 1246 58 38 367".split()

print(*range(1, 9))

for i in permutations("АБВГДЕЗЖ"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7 8
# А Б В Г Д Е Ж З


