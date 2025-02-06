with open("9-input.txt") as f:
    data = [list(map(int, l.split())) for l in f]

def f1(row):
    counts = [row.count(i) for i in row]
    if counts.count(3) == 3 and counts.count(1) == 4:
        return True
    return False

def f2(row):
    sort_row = sorted(row)
    if sort_row == row:
        return True
    return False

c = 0
for row in data:
    if (f1(row) + f2(row)) <= 1:
        c += 1

print(c)
