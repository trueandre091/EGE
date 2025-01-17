from itertools import permutations

graph = "AB BC CF FG GE EA DB DC DF DE DA".split()
mat = "23567 145 146 23 127 137 156".split()

print(*range(1, 8))

for i in permutations("ABCDEFG"):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

# 1 2 3 4 5 6 7
# D E F G A C B
# D F E G C A B
