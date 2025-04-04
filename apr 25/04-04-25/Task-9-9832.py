with open("9_9832.txt") as f:
    data = [list(map(int, i.split())) for i in f]

def f1(row):
    c = [row.count(i) for i in row]
    if c.count(2) == 4 and c.count(1) == 3:
        return True
    return False

def f2(row):
    if row.count(max(row)) == 1:
        return True
    return False

for row in data:
    if f1(row) and f2(row):
        print(sum(row))
        break



