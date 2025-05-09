with open("27.13.A_19567.txt") as f:
    dataA = []
    for l in f:
        x, y = l.replace(",", ".").split()
        dataA.append((float(x), float(y)))

with open("27.13.B_19567.txt") as f:
    dataB = []
    for l in f:
        x, y = l.replace(",", ".").split()
        dataB.append((float(x), float(y)))


from math import dist

klsA = [[], []]
klsB = [[], [], [], [], [], []]

for p in dataA:
    if p[1] > 0:
        klsA[0].append(p)
    else:
        klsA[1].append(p)

for p in dataB:
    if p[1] > (p[0] + 12):
        klsB[0].append(p)
    elif p[1] > 6.5 and p[0] < 4:
        klsB[1].append(p)
    elif p[1] > (p[0] + 4):
        klsB[2].append(p)
    elif p[1] > 4:
        klsB[3].append(p)
    elif p[1] > (p[0] - 2):
        klsB[4].append(p)
    else:
        klsB[5].append(p)

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
# 10770 8264
# B
# 3785 46909



