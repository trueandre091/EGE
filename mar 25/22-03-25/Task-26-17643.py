with open("26_17643.txt") as f:
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

from statistics import mean

av_price = mean([i[1] for i in data])

expensive = [i for i in data if i[1] > av_price]

articles = []
for j in data:
    if j not in expensive:
        continue
    i0 = j[0]
    i1 = j[1]
    i2 = 0
    i3 = 0
    for i in data:
        if i[0] == j[0]:
            if i[2]:
                i3 += 1
            else:
                i2 += 1

    articles.append((i0, i1, i2, i3))

articles = set(articles)
articles = sorted(articles, key=lambda x: (-x[2], -x[1], x[3]))

print(articles[:5])
leader = articles[0][0]
sum_sells = sum([i[1] for i in data if (i[0] == leader) and (i[2] == 0)])
print(sum_sells)
print(articles[0][3])

most_sell = sorted(expensive, key=lambda x: (x[0]))





