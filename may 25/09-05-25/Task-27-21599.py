with open("27_A_21599.txt") as f:
    dataA = []
    for l in f:
        x, y = l.replace(",", ".").split()
        dataA.append((float(x), float(y)))

with open("27_B_21599.txt") as f:
    dataB = []
    for l in f:
        x, y = l.replace(",", ".").split()
        dataB.append((float(x), float(y)))

from math import dist

klsA = [[] for i in range(3)]
klsB = [[] for i in range(6)]

for p in dataA:
    if p[1] > (p[0] - 10):
        klsA[0].append(p)
    elif p[1] > (0.5 * p[0] - 12.5):
        klsA[1].append(p)
    else:
        klsA[2].append(p)

for p in dataB:
    if p[1] < (-2 * p[0] - 26):
        klsB[0].append(p)
    elif p[0] < -10:
        klsB[1].append(p)
    elif p[1] > (2 * p[0] + 14):
        klsB[2].append(p)
    elif p[1] > ((2 / 3) * p[0]):
        klsB[3].append(p)
    elif p[1] > -4.5:
        klsB[4].append(p)
    else:
        klsB[5].append(p)

print([len(kl) for kl in klsA])
print([len(kl) for kl in klsB])

def center(kl):
    kl_r = [(sum(dist(c, p) for p in kl), c) for c in kl]
    return min(kl_r)[1]

csA = [center(kl) for kl in klsA]
csB = [center(kl) for kl in klsB]

print(sum(c[0] for c in csA) / len(csA) * 10000)
print(sum(c[1] for c in csA) / len(csA) * 10000)
print(sum(c[0] for c in csB) / len(csB) * 10000)
print(sum(c[1] for c in csB) / len(csB) * 10000)

# A
# 178755 2896
# B
# 37392 50998






