from itertools import permutations

graph = "АБ БГ ГЕ ЕЗ ЗЖ ЖД ДГ ГВ ВА ГА ГЗ ГЖ".split()
mat = "235 13 1245678 36 13 347 368 37".split()

print(*range(1, 9))

for i in permutations("АБВГДЕЗЖ"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7 8
# А Б Г Д В Ж З Е

# 16 + 17 + 11 = 44



