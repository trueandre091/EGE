from itertools import permutations

graph = "АБ БГ ГЕ ЕЗ ЗД ГД ДВ БВ ВА".split()
matrix = "67 567 456 35 234 123 12".split()

print(*range(1, 8))

for i in permutations("АБВГДЕЗ"):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

# ГЕ + ДЗ = 12 + 9 = 21