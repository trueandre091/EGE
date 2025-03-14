with open("9_18174.txt") as f:
    data = [list(map(int, i.split())) for i in f]

def f1(row):
    c = [row.count(i) for i in row]
    if (c.count(2) == 2) and (c.count(1) == 4):
        return True
    return False

def f2(row):
    otr = [i for i in row if i < 0]
    pol = [i for i in row if i > 0]
    if abs(sum(otr)) > sum(pol):
        return True
    return False


k = 0
for row in data:
    if f1(row) and f2(row):
        k += 1

print(k)

