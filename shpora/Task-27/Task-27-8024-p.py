with open("27-8024b.txt") as f:
    data = []
    for l in f:
        x, y = l.replace(",", ".").split()
        data.append((float(x), float(y)))

from math import dist

kls = []
eps = 1
while data:
    kl = [data.pop()]
    for p1 in kl:
        for p2 in data.copy():
            if dist(p1, p2) <= eps:
                kl.append(p2)
                data.remove(p2)
    kls.append(kl)

print([len(kl) for kl in kls])

def mid(kl, ax):
    all_x = [i[ax] for i in kl]
    for x in all_x:
        left, right = 0, 0
        for i in kl:
            if i[ax] < x: left += 1
            if i[ax] > x: right += 1

        if left == right:
            return x

mids = [(mid(kl, 0), mid(kl, 1)) for kl in kls]

print(sum(m[0] for m in mids) / len(mids) * 10000)
print(sum(m[1] for m in mids) / len(mids) * 10000)





