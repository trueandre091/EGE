from itertools import combinations

def f(x):
    P = 69 <= x <= 91
    Q = 77 <= x <= 114
    A = A1 <= x <= A2
    return Q <= ((P == Q) or ((not P) <= A))

line = []
for i in [69, 77, 91, 114]:
    line += [i - 0.1, i, i + 0.1]
ans = []

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(min(ans))


