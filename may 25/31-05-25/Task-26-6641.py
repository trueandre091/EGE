with open("26_6641.txt") as f:
    N, M = map(int, f.readline().split())
    data = []
    for i in f:
        i = i.split()
        data.append((int(i[0]), i[1]))

data = sorted(data)
goods_S, goods_W = [], []

for good in data.copy():
    if good[0] <= M:
        M -= good[0]
        if good[1] == "S":
            goods_S.append(good)
        else:
            goods_W.append(good)
        data.remove(good)

print(len(goods_S), M)

data_S = [i for i in data if i[1] == "S"]

for good in data_S:
    if M + goods_W[-1][0] - good[0] >= 0:
        M += goods_W[-1][0] - good[0]
        goods_S.append(good)
        goods_W.pop()

print(len(goods_S), M)
