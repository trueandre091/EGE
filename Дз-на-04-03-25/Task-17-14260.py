with open("17_14260.txt") as f:
    data = [int(i) for i in f]

a = []
minn = min(i for i in data if (i > 0) and (1000 <= abs(i) <= 9999) and (len(set(str(i)[-2:]))) == 1)

for t in zip(data, data[1:], data[2:]):
    if all((100 <= abs(t[i]) <= 999) for i in range(3)):
        if sum(t) > minn:
            a.append(sum(t))

print(len(a), max(a))

# 8 1958


