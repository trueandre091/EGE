with open("9_6262.txt") as f:
    data = [list(map(int, i.split())) for i in f]

def f1(row):
    counts = [row.count(i) for i in row]
    return sum(counts) > 6

def f2(row):
    nech = [i for i in row if i % 2 != 0]
    return len(nech) == 3

c = 0
for row in data:
    if f1(row) ^ f2(row):
        c += 1

print(c)



