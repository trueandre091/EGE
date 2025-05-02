with open("27_A_17916.txt") as f:
    f.readline()
    data = []
    for l in f:
        x, y = l.replace(",", ".").split()
        data.append((float(x), float(y)))

kl1, kl2 = [], []
for p in data:
    if p[1] < 8:
        kl1.append(p)
    else:
        kl2.append(p)

def r(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

def center(kl):
    kl_r = []
    for c in kl:
        c_r = 0
        for p in kl:
            c_r += r(c, p)
        kl_r.append((c_r, c))
    return min(kl_r)[1]

c1 = center(kl1)
c2 = center(kl2)

print((c1[0] + c2[0]) / 2 * 10000)
print((c1[1] + c2[1]) / 2 * 10000)


