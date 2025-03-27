# with open("27_A-input.txt") as f:
#     f.readline()
#     data = []
#     for p in f:
#         x, y = p.split()
#         x = float(x.replace(",", "."))
#         y = float(y.replace(",", "."))
#         data.append((x, y))
#
# kl1, kl2 = [], []
# for p in data:
#     if (0 < p[0] < 5) and (4 < p[1] < 10):
#         kl1.append(p)
#     else:
#         kl2.append(p)
#
# def r(p1, p2):
#     return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
#
# def centre(kl):
#     cs = []
#     for c in kl:
#         summ = 0
#         for p in kl:
#             if c == p:
#                 continue
#             summ += r(c, p)
#         cs.append((summ, c))
#     c = min(cs)[1]
#     return c
#
# c1 = centre(kl1)
# c2 = centre(kl2)
#
# from statistics import mean
#
# print(mean([c1[0], c2[0]]) * 10000)
# print(mean([c1[1], c2[1]]) * 10000)


with open("27_B-input.txt") as f:
    f.readline()
    data = []
    for p in f:
        x, y = p.split()
        x = float(x.replace(",", "."))
        y = float(y.replace(",", "."))
        data.append((x, y))

kl1, kl2, kl3 = [], [], []
for p in data:
    if (-1 < p[0] < 8) and (-1 < p[1] < 7):
        kl1.append(p)
    elif (-2 < p[0] < 6) and (-14 < p[1] < -5):
        kl2.append(p)
    else:
        kl3.append(p)

def r(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

def centre(kl):
    cs = []
    for c in kl:
        summ = 0
        for p in kl:
            if c == p:
                continue
            summ += r(c, p)
        cs.append((summ, c))
    c = min(cs)[1]
    return c

c1 = centre(kl1)
c2 = centre(kl2)
c3 = centre(kl3)
print(c1, c2, c3)

from statistics import mean

print(mean([c1[0], c2[0], c3[0]]) * 10000)
print(mean([c1[1], c2[1], c3[1]]) * 10000)

