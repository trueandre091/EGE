with open("27_B_21931.txt") as f:
    data = []
    for l in f:
        x, y = l.replace(",", ".").split()
        data.append((float(x), float(y)))

from math import dist

eps = 1
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
    kl_r = [(sum(dist(c, p) for p in kl), c) for c in kl]
    return max(kl_r)[1]

cs = [(len(kl), center(kl)) for kl in kls]
print(min(cs)[1][0] * 10000)
print(max(cs)[1][1] * 10000)


