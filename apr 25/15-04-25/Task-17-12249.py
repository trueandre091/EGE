with open("17_12249.txt") as f:
    data = [int(i) for i in f]

maxx = max(i for i in data if (10000 <= abs(i) <= 99999) and str(i)[-1] == "3")

a = []
for t in zip(data, data[1:], data[2:]):
    if any(str(i)[-1] == "3" for i in t):
        if sum(t) <= maxx:
            a.append(sum(t))


print(len(a), max(a))

