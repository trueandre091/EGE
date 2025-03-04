with open("17_9786.txt") as f:
    data = [int(i) for i in f]

maxx = max(i for i in data if str(i)[-2:] == "25")

def f1(pair):
    if ((1000 <= abs(pair[0]) <= 9999) + (1000 <= abs(pair[1]) <= 9999) + (1000 <= abs(pair[2]) <= 9999)) <= 2:
        return True
    return False

def f2(pair):
    if sum(pair) <= maxx:
        return True
    return False

a = []
for i in range(len(data) - 2):
    pair = data[i:i+3]
    if f1(pair) and f2(pair):
        a.append(sum(pair))

print(len(a), max(a))




