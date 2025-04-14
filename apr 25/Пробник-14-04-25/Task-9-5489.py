with open("9_5489.txt") as f:
    data = [list(map(int, i.split())) for i in f]

def f1(row):
    cs = [row.count(i) for i in row]
    return cs.count(1) == 5

def f2(row):
    ch = [i for i in row if i % 2 == 0]
    nech = [i for i in row if i % 2 != 0]
    return len(ch) > len(nech)

def f3(row):
    ch = [i for i in row if i % 2 == 0]
    nech = [i for i in row if i % 2 != 0]
    return sum(ch) < sum(nech)

c = 0
for row in data:
    if f1(row) and f2(row) and f3(row):
        c += 1

print(c)



