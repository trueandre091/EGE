from itertools import combinations

def f(x):
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    A = A1 <= x <= A2
    return (not ((not P) <= Q)) <= (A <= ((not Q) <= P))

ans = []
line = [i / 5 for i in range(10 * 5, 26 * 5)]

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(max(ans))