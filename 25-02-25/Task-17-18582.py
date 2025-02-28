with open("17_18582.txt") as f:
    data = [int(i) for i in f]


minn = min(i for i in data)

def f(t):
    otr = [i for i in t if i < 0]
    pol = [i for i in t if i > 0]
    if len(otr) > len(pol):
        summ = sum(t)
        if str(summ)[-1] == str(minn)[-1]:
            return True
    return False

ans = []
for t in zip(data, data[1:], data[2:]):
    if f(t):
        ans.append(abs(sum(t)))

print(len(ans), max(ans))


