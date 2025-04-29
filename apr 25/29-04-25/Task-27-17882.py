from statistics import mean

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

# A
with open("27_A_17882.txt") as f:
    dataA = []
    for l in f:
        x, y = l.replace(",", ".").split()
        x, y = float(x), float(y)
        dataA.append((x, y))

kl1, kl2 = [], []
for p in dataA:
    if p[1] < 3:
        kl1.append(p)
    else:
        kl2.append(p)

c1 = center(kl1)
c2 = center(kl2)
print(mean([c1[0], c2[0]]) * 10000)
print(mean([c1[1], c2[1]]) * 10000)

# B
with open("27_B_17882.txt") as f:
    dataB = []
    for l in f:
        x, y = l.replace(",", ".").split()
        x, y = float(x), float(y)
        dataB.append((x, y))

kl1, kl2, kl3 = [], [], []
for p in dataB:
    if p[1] < 4:
        kl1.append(p)
    elif 4 < p[1] < 7.5:
        kl2.append(p)
    else:
        kl3.append(p)

c1 = center(kl1)
c2 = center(kl2)
c3 = center(kl3)

print(mean([c1[0], c2[0], c3[0]]) * 10000)
print(mean([c1[1], c2[1], c3[1]]) * 10000)

























