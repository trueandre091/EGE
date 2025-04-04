with open("9_4614.txt") as f:
    data = [list(map(int, i.split())) for i in f]

def f1(row):
    if max(row) < (sum(row) - max(row)):
        return True
    return False

def f2(row):
    counts = [row.count(i) for i in row]
    if counts.count(2) == 2 and counts.count(1) == 2:
        return True
    return False

c = 0
for row in data:
    if f1(row) and f2(row):
        c += 1

print(c)

