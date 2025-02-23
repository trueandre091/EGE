with open("9-input.txt") as f:
    data = [list(map(int, i.split())) for i in f]

def f1(row):
    counts = [row.count(i) for i in row]
    if counts.count(3) == 3 and counts.count(1) == 4:
        return True
    return False

def f2(row):
    ch = [i for i in row if i % 2 == 0]
    nech = [i for i in row if i % 2 != 0]
    if len(ch) > len(nech):
        return True
    return False

for pos, row in enumerate(data, 1):
    if f1(row) and f2(row):
        print(pos, row)




