with open("27_B_20816.txt") as f:
    f.readline()
    data = []
    for i in f:
        i = tuple(map(float, i.replace(",", ".").split()))
        data.append(i)

from statistics import mean

def r(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

# kl1, kl2 = [], []
# for p in data:
#     if p[1] > 0:
#         kl1.append(p)
#     else:
#         kl2.append(p)

kl1, kl2, kl3 = [], [], []
for p in data:
    if (-1 < p[1] < 7) and (-1 < p[0] < 8):
        kl1.append(p)
    if (-14 < p[1] < -5) and (-2 < p[0] < 6):
        kl2.append(p)
    if (-15 < p[0] < -6) and (-9 < p[1] < 0):
        kl3.append(p)

def center(kl):
    l = []
    for c in kl:
        l.append(0)
        for p in kl:
            l[-1] += r(c, p)
    return kl[l.index(min(l))]


c1 = center(kl1)
c2 = center(kl2)
c3 = center(kl3)
print(mean([c1[0], c2[0], c3[0]])*10000)
print(mean([c1[1], c2[1], c3[1]])*10000)
