with open("27_A_21911.txt") as f:
    f.readline()
    data = []
    for l in f:
        x, y = l.replace(",", ".").split()
        data.append((float(x), float(y)))

from math import dist

eps = 2
kls = []
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
    kl_r = []
    for c in kl:
        c_r = 0
        for p in kl:
            c_r += dist(c, p)
        kl_r.append((c_r, c))
    return min(kl_r)[1]

c1 = center(kls[0])
c2 = center(kls[1])

print((c1[0] + c2[0]) / 2 * 10000)
print((c1[1] + c2[1]) / 2 * 10000)
