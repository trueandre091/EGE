with open("9-input.txt") as f:
    data = [list(map(int, l.split())) for l in f]


def f1(row):
    counts = [row.count(i) for i in row]
    if counts.count(2) == 2 and counts.count(1) == 4:
        return True
    return False

def f2(row):
    sum_ot = sum(i for i in row if i < 0)
    sum_pol = sum(i for i in row if i > 0)
    if abs(sum_ot) > sum_pol:
        return True
    return False

c = 0
for row in data:
    if f1(row) and f2(row):
        c += 1

print(c)

