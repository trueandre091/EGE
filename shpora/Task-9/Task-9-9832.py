with open("9-9832.txt") as f:
    data = [list(map(int, i.split())) for i in f]

def f1(row):
    cs = [row.count(i) for i in row]
    return cs.count(2) == 4 and cs.count(1) == 3

def f2(row):
    maxx = max(row)
    return row.count(maxx) == 1


for row in data:
    if f1(row) and f2(row):
        print(sum(row))
        break


