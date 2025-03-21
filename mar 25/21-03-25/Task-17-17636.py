with open("17_17636.txt") as f:
    data = [int(i) for i in f]

maxx = max(i for i in data if (str(i)[-1] == "3") and (100 <= abs(i) <= 999))

a = []
for t in zip(data, data[1:], data[2:]):
    u = any((100 <= abs(i) <= 999) and (str(i)[-1] == "3") for i in t)
    u1 = sum(t) < maxx
    if u and u1:
        a.append(sum(t))

print(len(a), max(a))








