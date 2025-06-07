with open("27-8022b.txt") as f:
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

def d(kl):
    kl_r = []
    for p1 in kl:
        for p2 in kl:
            kl_r.append((dist(p1, p2), [p1, p2]))
    return max(kl_r)[1]

ds = []
for kl in kls: ds += d(kl)

print(sum(p[0] for p in ds) / len(ds) * 10000)
print(sum(p[1] for p in ds) / len(ds) * 10000)
