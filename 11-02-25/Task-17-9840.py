with open("17_9840.txt") as f:
    data = [int(i) for i in f]

maxx = max(i for i in data if (1000 <= abs(i) <= 9999) and (str(abs(i))[-2:] == "39"))

def f1(pair):
    if (1000 <= abs(pair[0]) <= 9999) + (1000 <= abs(pair[1]) <= 9999) == 1:
        return True
    return False

def f2(pair):
    if sum(pair)**2 <= maxx**2:
        return True
    return False

a = []
for i in range(len(data) - 1):
    pair = data[i:i+2]
    if f1(pair) and f2(pair):
        a.append(sum(pair))

print(len(a), max(a))




