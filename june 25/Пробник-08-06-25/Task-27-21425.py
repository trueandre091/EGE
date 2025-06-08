with open("27_B_21425.txt") as f:
    data = []
    for l in f:
        x, y = l.replace(",", ".").split()
        data.append((float(x), float(y)))

from math import dist

kls = []
eps = 3
while data:
    kl = [data.pop()]
    for p1 in kl:
        for p2 in data.copy():
            if dist(p1, p2) <= eps:
                kl.append(p2)
                data.remove(p2)
    kls.append(kl)

print([len(kl) for kl in kls])

def cen(kl):
    kl_r = [(sum(dist(p, c) for p in kl), c) for c in kl]
    return min(kl_r)[1]

cs = [cen(kl) for kl in kls]
print(sum(c[0] for c in cs) / len(cs) * 10000)
print(sum(c[1] for c in cs) / len(cs) * 10000)

