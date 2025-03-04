with open("17_5758.txt") as f:
    data = [int(i) for i in f]

m = set(data)
moda = (-1, -1)
for n in m:
    c = data.count(n)
    if c > moda[-1]:
        moda = (n, c)
moda = moda[0]


a = []
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        pair = sorted((data[i], data[j]))
        if (j + i) % 2 == 0:
            if pair[0] < moda < pair[1]:
                vars = [abs(moda - pair[0]), abs(moda - pair[1])]
                a.append(max(vars))

print(len(a), max(a))










