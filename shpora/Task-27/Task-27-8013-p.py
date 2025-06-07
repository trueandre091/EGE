with open("27-8013b.txt") as f:
    data = []
    for l in f:
        x, y = l.replace(",", ".").split()
        data.append((float(x), float(y)))

from math import dist

kls = []
eps = 0.4
while data:
    kl = [data.pop()]
    for p1 in kl:
        for p2 in data.copy():
            if dist(p1, p2) <= eps:
                kl.append(p2)
                data.remove(p2)
    kls.append(kl)

print([len(kl) for kl in kls])

from itertools import combinations

def av_s(kl):
    rs = []
    for p1, p2 in combinations(kl, 2):
        rs.append(dist(p1, p2))
    return sum(rs) / len(rs)

ss = [av_s(kl) for kl in kls]
print(min(ss) * 100000, max(ss) * 100000)


