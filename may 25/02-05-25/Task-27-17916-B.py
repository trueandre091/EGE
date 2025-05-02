with open("27_B_17916.txt") as f:
    f.readline()
    data = []
    for l in f:
        x, y = l.replace(",", ".").split()
        data.append((float(x), float(y)))

kl1, kl2, kl3, kl4, kl5 = [[] for i in range(5)]
for p in data:
    if p[1] < 1.9:
        kl1.append(p)
    elif p[1] < 4:
        kl2.append(p)
    elif p[1] < 9:
        kl3.append(p)
    elif p[1] < 13:
        kl4.append(p)
    else:
        kl5.append(p)

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
c3 = center(kl3)
c4 = center(kl4)
c5 = center(kl5)

print((c1[0] + c2[0] + c3[0] + c4[0] + c5[0]) / 5 * 10000)
print((c1[1] + c2[1] + c3[1] + c4[1] + c5[1]) / 5 * 10000)


