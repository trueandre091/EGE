with open("9_17628.txt") as f:
    data = [list(map(int, i.split())) for i in f]

def f1(row):
    minn = min(row)
    maxx = max(row)
    summ2 = sum(row) - minn - maxx
    if (minn + maxx) <= summ2:
        return True
    return False

c = 0
for row in data:
    if f1(row):
        c += 1

print(c)







