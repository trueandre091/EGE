with open("9_18174.txt") as f:
    data = [list(map(int, i.split())) for i in f]

def f1(row):
    counts = [row.count(i) for i in row]
    return counts.count(2) == 2 and counts.count(1) == 4

def f2(row):
    otr = [i for i in row if i < 0]
    pol = [i for i in row if i > 0]
    return abs(sum(otr)) > abs(sum(pol))


c = 0
for row in data:
    if f1(row) and f2(row):
        c += 1

print(c)
