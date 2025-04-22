with open('17_9840.txt') as f:
    data = [int(i) for i in f]

maxx = max(i for i in data if (1000 <= abs(i) <= 9999) and str(i)[-2:] == "39")

a = []
for p in zip(data, data[1:]):
    u1 = 1000 <= abs(p[0]) <= 9999
    u2 = 1000 <= abs(p[1]) <= 9999
    u3 = sum(p)**2 <= maxx**2
    if (u1 ^ u2) and u3:
        a.append(sum(p))

print(len(a), max(a))





