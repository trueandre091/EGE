with open("27A_18678.txt") as f:
    dataA = []
    for l in f:
        x, y = l.replace(",", ".").split()
        dataA.append((float(x), float(y)))

with open("27B_18678.txt") as f:
    dataB = []
    for l in f:
        x, y = l.replace(",", ".").split()
        dataB.append((float(x), float(y)))

from math import dist

klsA = [[] for i in range(2)]
klsB = [[] for i in range(3)]

for p in dataA:
    if p[1] > 2.5:
        if 1 < p[0] < 6:
            klsA[0].append(p)
    else:
        klsA[1].append(p)

for p in dataB:
    if (3.25 < p[0] < 6.25) and (1.5 < p[1] < 7):
        klsB[0].append(p)
    elif p[0] < 4.25 and (-1 < p[1] < 8.5):
        klsB[1].append(p)
    elif (-1.5 < p[1] < 10.5) and (not ((8.75 < p[0] < 9.25) and (p[1] > 9))):
        klsB[2].append(p)

print([len(kl) for kl in klsA])
print([len(kl) for kl in klsB])

def center(kl):
    kl_r = [(sum(dist(c, p) for p in kl), c) for c in kl]
    return min(kl_r)[1]

csA = [center(kl) for kl in klsA]
csB = [center(kl) for kl in klsB]

print(sum(c[0] for c in csA) / len(csA) * 100000)
print(sum(c[1] for c in csA) / len(csA) * 100000)
print(sum(c[0] for c in csB) / len(csB) * 100000)
print(sum(c[1] for c in csB) / len(csB) * 100000)

# A
# 346070 215898
# B
# 455364 406022
