from itertools import *

def f(x):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = A1 <= x <= A2
    return P <= ((Q and (not A)) <= (not P))

line = [x + e for x in range(100) for e in (-0.1, 0, 0.1)]
ans = []

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(min(ans))
