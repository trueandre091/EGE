with open("27B_18050.txt") as f:
    f.readline()
    data = []
    for line in f:
        x, y = line.replace(",", ".").split()
        x = float(x)
        y = float(y)
        data.append((x, y))

kl1, kl2, kl3 = [], [], []

for p in data:
    if 2.5 < p[0] < 4.7 and 7.43 < p[1] < 9.8:
        kl1.append(p)
    elif 4.12 < p[0] < 6.21 and 4.8 < p[1] < 7.4:
        kl2.append(p)
    else:
        kl3.append(p)

from statistics import mean

def r(p1, p2):
    return ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)**0.5

def center(kl):
    kl_r = []
    for c in kl:
        c_r = []
        for p in kl:
            if c == p:
                continue
            c_r.append(r(c, p))
        kl_r.append((sum(c_r), c))
    return min(kl_r)[1]

c1 = center(kl1)
c2 = center(kl2)
c3 = center(kl3)

print(mean([c1[0], c2[0], c3[0]])*10000)
print(mean([c1[1], c2[1], c3[1]])*10000)

