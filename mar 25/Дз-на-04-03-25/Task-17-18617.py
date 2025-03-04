with open("17_18617.txt") as f:
    data = [int(i) for i in f]

maxx = max(data)
minn = min(data)

a = []
for p in zip(data, data[1:]):
    if any((p[i] % 3) == (maxx % 3) for i in range(2)):
        if any((p[i] % 7) == (minn % 7) for i in range(2)):
            a.append(sum(p))

print(len(a), max(a))

# 1467 197700