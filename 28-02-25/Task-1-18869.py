from itertools import permutations

graph = 'HA AB BC CD DE EH GH GA GF FE FC'.split()
mat = '568 36 247 368 178 124 35 145'.split()

print(*range(1, 9))

for i in permutations("ABCDEFGH"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7 8
# H D C F A E B G

# 64815