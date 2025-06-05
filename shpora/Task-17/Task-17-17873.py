with open("17_17873.txt") as f:
    data = [int(i) for i in f]

minn = min(data)

a = []
for p in zip(data, data[1:]):
    if any(abs(i) % 16 == minn for i in p):
        a.append(sum(p))


print(len(a), max(a))

