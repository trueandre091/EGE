with open("26-19726.txt") as f:
    N = int(f.readline())
    data = [list(map(int, l.split())) for l in f]


data = sorted(data, key=lambda x: (x[1], -x[0]))

res = [data[0]]
for met in data:
    if res[-1][1] <= met[0]:
        res.append(met)

print(len(res), res[-1][1])




