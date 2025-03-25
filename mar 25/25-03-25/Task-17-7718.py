with open("17_7718.txt") as f:
    data = [int(i) for i in f]

from itertools import combinations

a = []
for p in combinations(data, 2):
    u1 = sum(p) % 18 == 0

    pr = p[0] * p[1]
    u2 = pr % 18 == 0

    if (u1 ^ u2):
        a.append(sum(p))

print(len(a), max(a))









