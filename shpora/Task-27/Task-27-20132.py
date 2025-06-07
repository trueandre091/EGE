with open("27B_1_20132.txt") as f:
    data = []
    for l in f:
        x, y = l.replace(",", ".").split()
        data.append((float(x), float(y)))

from math import dist

kls = []
eps = 1
while data:
    kl = [data.pop()]
    for p1 in kl:
        for p2 in data.copy():
            if dist(p1, p2) <= eps:
                kl.append(p2)
                data.remove(p2)
    kls.append(kl)

print([len(kl) for kl in kls])

def f(kl1, kl2):
    kl_r = []
    for p1 in kl1:
        for p2 in kl2:
            kl_r.append((dist(p1, p2), (p1, p2)))
    return min(kl_r)[1]

from itertools import combinations

corners = set()
for kl1, kl2 in combinations(kls, 2):
    corners |= {*f(kl1, kl2)}

print(sum(c[0] for c in corners) / len(corners) * 10000)
print(sum(c[1] for c in corners) / len(corners) * 10000)





