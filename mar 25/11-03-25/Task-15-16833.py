from itertools import combinations

def f(x):
    P = 25 <= x <= 73
    Q = 75 <= x <= 118
    A = A1 <= x <= A2
    return (A and (not Q)) <= (P or Q)

line = []
for i in [25, 73, 75, 118]:
    line += [i-0.1, i, i+0.1]
ans = []

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(max(ans))

# 48




