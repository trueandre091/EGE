with open("26var01.txt") as f:
    N, M, K = list(map(int, f.readline().split()))
    data = [list(map(int, i.split())) for i in f]

data = sorted(data, key = lambda x: (x[1], -x[0]))

pole = [M + 1] * (K + 1)
for h,v in data:
    pole[v] = h

ans = []
for i in range(1, len(pole) - 1):
    ans.append((min(pole[i], pole[i + 1]) - 1, i))

print(max(ans, key=lambda x: x[0]))













