with open("9-input.txt") as f:
    data = [list(map(int, i.split())) for i in f]

def f1(row):
    counts = [row.count(i) for i in row]
    if (counts.count(2) == 2) and (counts.count(1) == 5):
        return True
    return False

def f2(row):
    pov = [i for i in row if row.count(i) > 1]
    nepov = [i for i in row if row.count(i) == 1]
    if sum(pov)**2 > sum(nepov)**2:
        return True
    return False

for row in data:
    if f1(row) and f2(row):
        print(sum(row), row)
        break


