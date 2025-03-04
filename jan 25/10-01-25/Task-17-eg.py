with open("17-input.txt") as f:
    data = [int(i) for i in f]

max_68 = max([i for i in data if str(i)[-2:] == "68"])
a = []
for i in range(len(data) - 3):
    c = data[i:i+4]
    u1 = [len(str(abs(k))) == 2 for k in c]
    u2 = sum(u1) == 1 or sum(u1) == 4
    summ = sum(c)
    u3 = summ >= max_68
    if u2 and u3:
        a.append(summ)

print(len(a), max(a))




