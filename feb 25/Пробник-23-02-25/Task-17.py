with open("17-input.txt") as f:
    data = [int(i) for i in f]

maxx = max(i for i in data if str(i)[-2:] == "50")
print(maxx)

ans = []
for p in zip(data, data[1:], data[2:]):
    u1 = (p[0] != p[1]) and (p[0] != p[2]) and (p[1] != [2])
    u2 = all(10000 <= abs(p[i]) <= 99999 for i in range(3))
    summ = sum(p)
    if summ <= maxx and all([u1, u2]):
        ans.append(summ)
        print(p)

print(len(ans), max(ans))



