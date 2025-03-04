with open("17-input.txt") as f:
    data = [int(i) for i in f]


def f1(row):
    dv = 0
    for n in row:
        if len(str(abs(n))) == 2:
            dv += 1
    if dv == 1 or dv == 4:
        return True
    return False

def f2(row):
    summ = sum(row)
    maxx = -1
    for n in data:
        if str(n)[-2:] == "68":
            maxx = max(maxx, n)
    if summ >= maxx:
        return True
    return False

a = []
c = 0
for i in range(len(data) - 3):
    row = (data[i], data[i + 1], data[i + 2], data[1 + 3])
    if f1(row) and f2(row):
        a.append(sum(row))
        c += 1

print(c, max(a))






















    
    
