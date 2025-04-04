with open("9_17522.txt") as f:
    data = [list(map(int, i.split())) for i in f]

def f1(row):
    return max(row) < (sum(row) - max(row))

def f2(row):
    c = [row.count(i) for i in row]
    return c.count(2) == 2 and c.count(1) == 2

c = 0
for row in data:
    if f1(row) and f2(row):
        c += 1

print(c)
