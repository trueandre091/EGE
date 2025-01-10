with open("9-input.txt") as f:
    data = [list(map(int, i.split())) for i in f]

def f1(row):
    m = min(row)
    if row.count(m) == 1:
        return True
    return False

def f2(row):
    counts = [row.count(i) for i in row]
    if sum(counts) != 6:
        return True
    return False

def f3(row):
    maxx = max(row)
    minn = min(row)
    sum_pov = sum(i for i in row if row.count(i) > 1)
    if minn + maxx < sum_pov:
        return True
    return False

c = 0
for row in data:
    if f1(row) and f2(row) and f3(row):
        print(row)
        c += 1

print(c)
    
