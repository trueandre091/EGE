with open("9_9778.txt") as f:
    data = [list(map(int, i.split())) for i in f]

from statistics import mean

def f1(row):
    c = [row.count(i) for i in row]
    if c.count(2) == 2 and c.count(1) == 4:
        return True
    return False

def f2(row):
    pov = [i for i in row if row.count(i) > 1]
    nepov = [i for i in row if row.count(i) == 1]
    if pov[-1] >= mean(nepov):
        return True
    return False


for pos, row in enumerate(data, 1):
    if f1(row) and f2(row):
        print(pos)
        break




