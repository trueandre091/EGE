with open("17_14952.txt") as f:
    data = [int(i) for i in f]

maxx = max(i for i in data if str(i)[-3:] == "121")

def f1(t):
    c4 = [i for i in t if (1000 <= abs(i) <= 9999) and (i % 2 == 0)]
    if len(c4) <= 1:
        return True
    return False

def f2(t):
    if sum(t) <= maxx:
        return True
    return False

ans = []
for t in zip(data, data[1:], data[2:]):
    if f1(t) and f2(t):
        ans.append(sum(t))

print(len(ans), max(ans))










