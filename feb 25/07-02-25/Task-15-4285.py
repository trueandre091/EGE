from itertools import combinations

def f(x):
    P = 25 <= x <= 240
    Q = 175 <= x <= 300
    R = 270 <= x <= 340
    A = A1 <= x <= A2
    return (Q <= P) or ((not A) <= R)

ans = []
dots = [25, 175, 240, 270, 300, 340]
line = []
for x in dots: line += [x - 0.2, x, x + 0.2]

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(min(ans))

