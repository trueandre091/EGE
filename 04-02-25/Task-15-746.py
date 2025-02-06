from itertools import combinations

def f(x):
    P = 12 <= x <= 26
    Q = 30 <= x <= 53
    A = A1 <= x <= A2
    return (A <= P) or Q

ans = []
line = [1, 12, 26, 30, 53, 60]
for A1, A2 in combinations(line, 2):
    if all(f(x / 5) for x in range(A1*5 - 1, A2*5 + 1)):
        ans.append(A2 - A1)

print(max(ans))



