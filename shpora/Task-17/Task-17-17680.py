with open("17_17680.txt") as f:
    data = [int(i) for i in f]

minn = min(i for i in data if (i > 0) and (abs(i) % 41 == 0))

a = []
for p in zip(data, data[1:]):
    if p[0] != p[1]:
        if abs(p[1] - p[0]) % minn == 0:
            a.append(sum(p))

print(len(a), max(a))


