from itertools import permutations

graph = "CE EG GF FA AC CD DH HE AB BF".split()
mat = "68 47 45 237 368 15 248 157".split()

print(*range(1, 9))

for i in permutations("ABCDEFGH"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7 8
# D B G F E H A C

# 13 + 5 = 18

