with open("27A_20130.txt") as f:
    dataA = []
    for l in f:
        x, y = l.split()
        x, y = float(x.replace(',', ".")), float(y.replace(',', "."))
        dataA.append((x, y))

# A
kl1, kl2 = [], []

for p in dataA:
    if p[1] < 5:
        kl1.append(p)
    else:
        kl2.append(p)

def r(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def d(kl):
    kl_r = []
    for p1 in kl:
        for p2 in kl:
            if p1 == p2: continue
            kl_r.append((r(p1, p2), (p1, p2)))

    return max(kl_r)[1]

d1_p1, d1_p2 = d(kl1)
d2_p1, d2_p2 = d(kl2)

from statistics import mean

print(mean([d1_p1[0], d1_p2[0], d2_p1[0], d2_p2[0]]) * 10000, end=" ")
print(mean([d1_p1[1], d1_p2[1], d2_p1[1], d2_p2[1]]) * 10000)

# B
with open("27B_20130.txt") as f:
    dataB = []
    for l in f:
        x, y = l.split()
        x, y = float(x.replace(',', ".")), float(y.replace(',', "."))
        dataB.append((x, y))


kl1, kl2, kl3 = [], [], []

for p in dataB:
    if p[1] < 2:
        kl1.append(p)
    elif 2 < p[1] < 7:
        kl2.append(p)
    else:
        kl3.append(p)

d1_p1, d1_p2 = d(kl1)
d2_p1, d2_p2 = d(kl2)
d3_p1, d3_p2 = d(kl3)

from statistics import mean

print(mean([d1_p1[0], d1_p2[0], d2_p1[0], d2_p2[0], d3_p1[0], d3_p2[0]]) * 10000, end=" ")
print(mean([d1_p1[1], d1_p2[1], d2_p1[1], d2_p2[1], d3_p1[1], d3_p2[1]]) * 10000)





