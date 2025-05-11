from itertools import *

graph = "АБ БВ ВГ ГД ДЕ ЕБ БЖ ЖА БД ВД".split()
mat = "346 45 16 12567 24 1347 46".split()

print(*range(1, 8))

for i in permutations("АБВГДЕЖ"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# В А Г Б Ж Д Е
