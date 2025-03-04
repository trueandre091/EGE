with open("26-input.txt") as f:
    N = f.readline()
    data = []
    for i in f:
        i = list(map(int, i.split()))
        k = [i[0], i[0] + i[1]]
        data.append(k)

data = sorted(data, key=lambda x: (x[1], x[0]))

ans = [data[0]]
for i in data[1:]:
    if i[0] >= ans[-1][1]:
        ans.append(i)

print(len(ans), ans[-1][0] - ans[-2][1])