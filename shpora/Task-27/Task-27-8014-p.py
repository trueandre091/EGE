with open("27-8014b.txt") as f:
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

def ebani_p(kl):
    kl_c = []
    for c in kl:
        a = 0
        for p in kl:
            if dist(c, p) <= 1:
                a += 1
        kl_c.append((a, c))
    kl_c.sort(key=lambda x: -x[0])
    return max(kl_c)[1]

e_ps = [ebani_p(kl) for kl in kls]
print(sum(p[0] for p in e_ps) / len(e_ps) * 100000)
print(sum(p[1] for p in e_ps) / len(e_ps) * 100000)
