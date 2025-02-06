from itertools import combinations

def f(x):
    P = 43 <= x <= 49
    Q = 44 <= x <= 53
    A = A1 <= x <= A2
    return (A <= P) or Q

ans = []
line = [40, 43, 44, 45, 49, 50, 53, 60]

for A1, A2 in combinations(line, r=2):
    if all(f(x / 5) for x in range(A1*5 - 1, A2*5 + 1)):
        ans.append(A2-A1)

print(max(ans))




