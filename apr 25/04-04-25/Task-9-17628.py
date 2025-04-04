with open("9_17628.txt") as f:
    data = [list(map(int, i.split())) for i in f]

def f(row):
    return (max(row) + min(row)) <= sum(row) - (max(row) + min(row))

c = 0
for row in data:
    if f(row):
        c += 1

print(c)


