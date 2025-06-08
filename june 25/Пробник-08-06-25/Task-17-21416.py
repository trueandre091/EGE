with open("17_21416.txt") as f:
    data = [int(i) for i in f]

s = sum(i for i in data if i < 0)

a = []
for t in zip(data, data[1:], data[2:]):
    if (max(t) * min(t)) > s:
        a.append(sum(t))

print(len(a), max(a))


