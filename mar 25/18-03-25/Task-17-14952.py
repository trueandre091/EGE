with open("17_14952.txt") as f:
    data = [int(i) for i in f]

maxx = max(i for i in data if str(i)[-3:] == "121")

a = []
for t in zip(data, data[1:], data[2:]):
    u4 = [((1000 <= abs(i) <= 9999) and (i % 2 == 0)) for i in t]
    if (sum(u4) <= 1) and (sum(t) <= maxx):
        a.append(sum(t))

print(len(a), max(a))








