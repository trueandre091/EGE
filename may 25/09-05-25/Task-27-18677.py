with open("27B_18677.txt") as f:
    data = []
    for l in f:
        x, y = l.replace(',', ".").split()
        data.append((float(x), float(y)))

from math import dist

# A
# data = [p for p in data if (p[1] > (p[0] - 8)) and (not ((p[0] < 3) and (2 < p[1] < 3)))]
# B
# data = [p for p in data if (p[1] > -2) and (not ((p[0] < 4) and (p[1] > 8))) and (not ((p[0] > 10) and (p[1] > 8)))]

kls = []
eps = 1
while data:
    kl = [data.pop()]
    for p1 in kl:
        for p2 in data.copy():
            if dist(p1, p2) < eps:
                kl.append(p2)
                data.remove(p2)
    kls.append(kl)

print([len(kl) for kl in kls])

def center(kl):
    kl_r = [(sum(dist(c, p) for p in kl), c) for c in kl]
    return min(kl_r)[1]

cs = [center(kl) for kl in kls]

print(sum(c[0] for c in cs) / len(cs) * 100000)
print(sum(c[1] for c in cs) / len(cs) * 100000)

# A
# 528073 71781
# B
# 669946 370701

