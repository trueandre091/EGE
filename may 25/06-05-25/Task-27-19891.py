with open("27.3.A_19891.txt") as f:
    dataA = []
    for l in f:
        x, y = l.replace(',', ".").split()
        dataA.append((float(x), float(y)))

with open("27.3.B_19891.txt") as f:
    dataB = []
    for l in f:
        x, y = l.replace(',', ".").split()
        dataB.append((float(x), float(y)))

klsA = [[], []]
klsB = [[], [], [], []]
for p in dataA:
    if p[0] < 3:
        klsA[0].append(p)
    else:
        klsA[1].append(p)

for p in dataB:
    if p[1] < -2:
        klsB[0].append(p)
    elif p[1] < 2:
        if p[0] < 1:
            klsB[1].append(p)
        else:
            klsB[2].append(p)
    else:
        klsB[3].append(p)

from math import dist

def center(kl):
    kl_r = [(sum(dist(c, p) for p in kl), c) for c in kl]
    return min(kl_r)[1]

csA = [center(kl) for kl in klsA]
csB = [center(kl) for kl in klsB]

print(sum(c[0] for c in csA) / 2 * 10000)
print(sum(c[1] for c in csA) / 2 * 10000)
print(sum(c[0] for c in csB) / 4 * 10000)
print(sum(c[1] for c in csB) / 4 * 10000)





