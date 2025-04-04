with open("9_9740.txt") as f:
    data = [list(map(int, i.split())) for i in f]

from statistics import mean

def f1(row):
    c = [row.count(i) for i in row]
    if c.count(3) == 3 and c.count(1) == 4:
        return True
    return False

def f2(row):
    pov = [i for i in row if row.count(i) > 1]
    nepov = [i for i in row if row.count(i) == 1]
    if mean(nepov) <= pov[-1]:
        return True
    return False

c = 0
for row in data:
    if f1(row) and f2(row):
        c += 1

print(c)
