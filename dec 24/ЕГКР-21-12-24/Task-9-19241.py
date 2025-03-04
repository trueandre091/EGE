with open("9-input.txt") as f:
    data = [list(map(int, line.split(","))) for line in f]

def f1(row):
    counts = [row.count(i) for i in row]
    if counts.count(3) == 6 and counts.count(1) == 1:
        return True
    return False

def f2(row):
    rep_nums = [i for i in row if row.count(i) != 1]
    avg = sum(rep_nums) / len(rep_nums)
    if avg < (sum(row) - sum(rep_nums)):
        return True
    return False

for pos, row in enumerate(data, 1):
    if f1(row) and f2(row):
        print(pos, row)

# 17975

