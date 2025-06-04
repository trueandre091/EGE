from itertools import *

def f(x):
    P = 15 <= x <= 142
    Q = 38 <= x <= 167
    A = A1 <= x <= A2
    return Q <= (((not A) and P) <= (not Q))

line = [x + e for x in range(10, 200) for e in (-0.1, 0, 0.1)]
ans = []

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(min(ans))


