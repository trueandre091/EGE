with open("27_A_21931.txt") as f:
    dataA = []
    for l in f:
        x, y = l.replace(",", '.').split()
        dataA.append((float(x), float(y)))

with open("27_B_21931.txt") as f:
    dataB = []
    for l in f:
        x, y = l.replace(",", '.').split()
        dataB.append((float(x), float(y)))


from math import dist

klsA = [[] for i in range(2)]
klsB = [[] for i in range(3)]

for p in dataA:
    if p[1] < 10:
        klsA[0].append(p)
    else:
        klsA[1].append(p)

for p in dataB:
    if p[1] < 10:
        klsB[0].append(p)
    elif p[0] < 17:
        klsB[1].append(p)
    else:
        klsB[2].append(p)

def center(kl):
    kl_r = [(sum(dist(c, p) for p in kl), c) for c in kl]
    return max(kl_r)[1]

csA = [(len(kl), center(kl)) for kl in klsA]
csB = [(len(kl), center(kl)) for kl in klsB]
csA = sorted(csA)
csB = sorted(csB)
print(csA[0][1][0] * 10000, csA[-1][1][1] * 10000)
print(csB[0][1][0] * 10000, csB[-1][1][1] * 10000)

# A
# 1663 61127
# B
# 147474 61934


