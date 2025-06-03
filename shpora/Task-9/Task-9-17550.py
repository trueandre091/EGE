with open("9_17550.txt") as f:
    data = [list(map(int, i.split())) for i in f]

def f1(row):
    cs = [row.count(i) for i in row]
    return cs.count(3) == 3 and cs.count(1) == 3

def f2(row):
    pov = [i for i in row if row.count(i) > 1]
    nepov = [i for i in row if row.count(i) == 1]
    return sum(pov)**2 > sum(nepov)**2

c = 0
for row in data:
    if f1(row) and f2(row):
        c += 1

print(c)


