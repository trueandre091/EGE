with open("26_2651.txt") as f:
    f.readline()
    data = [list(map(int, i.split())) for i in f]


d = {k: set() for k in range(1961, 1992)}

for m in data:
    d[m[0]].add(m[1])

ans1 = 0
for year, m in d.items():
    ans1 += 8 - len(m)

print(ans1)

d = list(d.items())
d = sorted(d, key=lambda x: (len(x[1]), -x[0]))
print(d[0])






