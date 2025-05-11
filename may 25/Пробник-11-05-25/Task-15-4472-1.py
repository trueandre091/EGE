from itertools import *

def f(x):
    P = 254 <= x <= 800
    Q = 410 <= x <= 823
    A = A1 <= x <= A2
    return (P and (not A)) <= Q

line = []
for i in [254, 410, 800, 823]:
    line += [i - 1, i - 0.9, i - 0.1, i, i + 0.1, i + 0.9, i + 1]
ans = []

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(min(ans))


