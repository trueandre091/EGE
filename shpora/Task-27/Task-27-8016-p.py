with open("27-8016b.txt") as f:
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

def p(kl):
    kl_c = []
    for c in kl:
        a = 0
        for p in kl:
            if dist(c, p) <= 1:
                a += 1
        kl_c.append(a)
    return sum(kl_c) / len(kl_c)

ps = [p(kl) for kl in kls]

print(min(ps) * 100000, sum(ps) / len(ps) * 100000)
