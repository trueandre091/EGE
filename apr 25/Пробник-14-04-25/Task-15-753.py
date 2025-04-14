from itertools import combinations

def f(x):
    P = 5 <= x <= 30
    Q = 14 <= x <= 23
    A = A1 <= x <= A2
    return (P == Q) <= (not A)

line = []
for i in range(3, 31):
    line += [i - 0.1, i, i + 0.1]

a = []
for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        a.append(A2 - A1)

print(max(a))


