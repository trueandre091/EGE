with open("26_9793.txt") as f:
    N = int(f.readline())
    details = []
    c = 1
    for l in f:
        l = l.split()
        inf1 = [int(l[0]), c, 0]
        inf2 = [int(l[1]), c, 1]
        details.append(inf1)
        details.append(inf2)
        c += 1

details.sort()
transp = [[]] * N
last = 0

for time, pos, type in details:
    if pos in transp:
        continue
    if type == 0:
        for i in range(len(transp)):
            if not transp[i]:
                transp[i] = pos
                break
    else:
        for i in range(len(transp))[::-1]:
            if not transp[i]:
                transp[i] = pos
                break
    last = pos

print(last, transp.index(last))

