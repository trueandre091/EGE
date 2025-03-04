with open("26-4938.txt") as f:
    N, L = map(int, f.readline().split())
    data = [list(map(int, l.split())) for l in f]

data = sorted(data, key=lambda x: x[1])

res = [data[0]]
for met in data:
    if res[-1][1] <= met[0] and met[1] <= N:
        res.append(met)

print(len(res), res[-1][0])

