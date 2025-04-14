with open("17_6791.txt") as f:
    data = [int(i) for i in f]


minn = min(i for i in data if str(i)[-2:] == "68")

a = []
for p in zip(data, data[1:]):
    u1 = str(p[0])[-2:] == "68"
    u2 = str(p[1])[-2:] == "68"
    summ = p[0]**2 + p[1]**2
    if (u1 ^ u2) and (summ >= minn**2):
        a.append(summ)

print(len(a), max(a))


