from itertools import combinations

def f(x):
    P = 117 <= x <= 158
    Q = 129 <= x <= 180
    A = A1 <= x <= A2
    return P <= ((Q and (not A)) <= (not P))

ans = []
line = [x / 5 for x in range(115 * 5, 181 * 5)]

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(min(ans))


