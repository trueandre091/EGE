with open("9_20899.txt") as f:
    data = [list(map(int, i.split())) for i in f]

c = 0
for row in data:
    cs = [row.count(i) for i in row]
    if max(row) < (sum(row) - max(row)):
        if cs.count(2) == 2 and cs.count(1) == 2:
            c += 1

print(c)

