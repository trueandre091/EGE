with open("17_12735.txt") as f:
    data = [int(i) for i in f]

maxx = max(i for i in data if str(i)[-2:] == "09")

a = []
for t in zip(data, data[1:], data[2:]):
    u1 = sum([i % 7 == 0 for i in t]) == 2
    u2 = sum(t) < maxx
    if u1 and u2:
        a.append(t[0]*t[1]*t[2])

print(len(a), min(a))



