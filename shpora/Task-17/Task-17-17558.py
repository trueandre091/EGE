with open("17_17558.txt") as f:
    data = [int(i) for i in f]

c = len([i for i in data if abs(i) % 32 == 0])

a = []
for p in zip(data, data[1:]):
    if any(i < 0 for i in data):
        if sum(p) < c:
            a.append(sum(p))


print(len(a), max(a))

