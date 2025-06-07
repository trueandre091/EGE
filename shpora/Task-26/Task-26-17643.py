with open("26_17643.txt") as f:
    N = f.readline()
    data = [list(map(int, i.split())) for i in f]

average = sum(i[1] for i in data) / len(data)

uniq_exp_articles_prices = set((i[0], i[1]) for i in data if i[1] > average)
uniq_exp_articles_info = []
for art, price in uniq_exp_articles_prices:
    ables, sells = 0, 0
    for i in data:
        if i[0] == art:
            if i[2] == 0: sells += 1
            else: ables += 1
    uniq_exp_articles_info.append((art, price, ables, sells))

leader = max(uniq_exp_articles_info, key=lambda x: (x[3], x[1], -x[2]))
print(leader[3] * leader[1], leader[2])



