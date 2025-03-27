from itertools import permutations

graph = "EG GH HC CD DF FB BE AG AB AD AC".split()
mat = "36 478 178 258 46 158 23 2346".split()

print(*range(1, 9))
for i in permutations("ABCDEFGH"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7 8
# E C G D F B H A
# E D B C H G F A


