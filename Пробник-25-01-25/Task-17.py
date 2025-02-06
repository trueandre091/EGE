with open("17-input.txt") as f:
    data = [int(i) for i in f]

minn = min(i for i in data if len(str(abs(i))) == 2)


def check(p):
    p1_s = p[0] ** 2
    p2_s = p[1] ** 2
    f1 = False
    f2 = False
    if (p1_s < minn**2) and (str(p1_s)[-1] == "1"):
        f1 = True
    if (p2_s < minn**2) and (str(p2_s)[-1] == "1"):
        f2 = True
    if (f1 + f2) == 1:
        return True
    return False

a = []
for i in range(len(data) - 1):
    pair = (data[i], data[i + 1])
    summ = sum(pair)
    if summ >= 0:
        if check(pair):
            a.append(summ)
            # print(pair)

# print(minn)

print(len(a), min(a))





