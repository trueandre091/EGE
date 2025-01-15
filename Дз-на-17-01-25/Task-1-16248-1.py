from itertools import permutations

graph = "AB BC CE EG GF FD DA CA CD ED EF".split()
mat = "347 3456 1245 123 236 25 14".split()

print(*range(1, 8))

for i in permutations("ABCDEFG"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# F C D E A B G

# 42
