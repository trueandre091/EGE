from itertools import permutations

graph = "EH HG HB BG DB DE EA AF FC CG FD".split()
mat = "367 568 18 58 247 127 156 234".split()

print(*range(1, 9))

for i in permutations("ABCDEFGH"):
    if all([str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph]):
        print(*i)

# 19 + 11 = 30
