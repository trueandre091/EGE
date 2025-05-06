with open("27.17.B_19566.txt") as f:
    data = []
    for l in f:
        x, y = l.replace(",", ".").split()
        data.append((float(x), float(y)))

from math import dist

kls = []
eps = 4
while data:
    kl = [data.pop()]
    for p1 in kl:
        for p2 in data.copy():
            if dist(p1, p2) < eps:
                kl.append(p2)
                data.remove(p2)
    if len(kl) > 10:
        kls.append(kl)

print([len(kl) for kl in kls])

def cry(kl):
    kl_r = [(sum(dist(c, p) for p in kl), c) for c in kl]
    return max(kl_r)[1]

cries = [cry(kl) for kl in kls]
print(sum(c[0] for c in cries) / len(cries) * 10000)
print(sum(c[1] for c in cries) / len(cries) * 10000)







