with open("17_12450.txt") as f:
    data = [int(i) for i in f]


minn = min(i for i in data if i % 52 == 0)

a = []
for t in zip(data, data[1:], data[2:]):
    summ_ost = sum([i % 113 for i in t])
    if summ_ost == minn:
        a.append(sum(t))

print(len(a), max(a))

