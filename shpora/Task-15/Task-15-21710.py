from itertools import *

def f(x):
    B = 36 <= x <= 75
    C = 60 <= x <= 110
    A = A1 <= x <= A2
    return (not A) <= (B == C)

line = [x + e for x in range(10, 200) for e in (-0.1, 0, 0.1)]
ans = []

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(min(ans))

