with open("9_18134.txt") as f:
    data = [list(map(int, i.split())) for i in f]

def f1(row):
    cs = [row.count(i) for i in row]
    return cs.count(2) == 4 and cs.count(1) == 2

def f2(row):
    pov = [i for i in row if row.count(i) > 1]
    nepov = [i for i in row if row.count(i) == 1]
    s = 1
    for i in nepov: s *= i
    return max(pov)**2 > s

c = 0
for row in data:
    if f1(row) and f2(row):
        c += 1

print(c)


