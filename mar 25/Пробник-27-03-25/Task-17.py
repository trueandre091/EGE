with open("17-input.txt") as f:
    data = [int(i) for i in f]

minn = min(i for i in data if (str(i)[-2:] == "19") and (100 <= abs(i) <= 999))

a = []
for t in zip(data, data[1:], data[2:]):
    u1 = any((str(i)[-2:] == "19") and (10000 <= abs(i) <= 99999) for i in t)
    u2 = sum(t) > minn**2
    if u1 and u2:
        a.append(sum(t))

print(len(a), min(a))

