from itertools import *

def f(x):
    D = 7 <= x <= 68
    C = 29 <= x <= 100
    A = A1 <= x <= A2
    return D <= (((not C) and (not A)) <= (not D))


line = []
for i in [7, 29, 68, 100]:
    line += [i - 0.1, i, i + 0.1]
ans = []

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(min(ans))

