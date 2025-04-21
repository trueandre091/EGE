with open("17_2399.txt") as f:
    data = [int(i) for i in f]

d35 = "".join([str(i) for i in data if i % 35 == 0])
summ = sum(map(int, d35))
print(summ)

def f1(p):
    if (p[0] > summ) and (p[1] <= summ):
        return hex(p[1])[-2:] == "ef"
    elif (p[1] > summ) and (p[0] <= summ):
        return hex(p[0])[-2:] == "ef"
    else:
        return False


a = []
for p in zip(data, data[1:]):
    if f1(p):
        a.append(sum(p))

print(len(a), min(a))



