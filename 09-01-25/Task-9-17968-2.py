with open("9-input.txt") as f:
    data = [list(map(int, i.split(","))) for i in f]

def f1(row):
    if max(row) < sum([i for i in row if i != max(row)]):
        return True
    return False

def f2(row):
    if sum([i for i in row if i % 2 == 0]) == sum([i for i in row if i % 2 != 0]):
        return True
    return False

c = 0
for row in data:
    if f1(row) and f2(row):
        c += 1

print(c)

# 13