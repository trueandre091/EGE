with open("26_17643.txt") as f:
    N = f.readline()
    data = [list(map(int, i.split())) for i in f]


uniq_articles_prices = list(set((i[0], i[1]) for i in data))
uniq_prices = [i[1] for i in uniq_articles_prices]

average = sum(uniq_prices) / len(uniq_prices)

uniq_exp_articles_prices = set(i[0] for i in data if i[1] > average)
uniq_exp_articles_info = []
for art in uniq_exp_articles:
    ables, sells = 0, 0
    for i in data:
        if i[0] == art:
            if i[2] == 1: sells += 1
            else: ables += 1
    uniq_exp_articles_info.append((art, ables, sells))

uniq_exp_articles_info.sort(key=lambda x: (-x[1], -x[1]))



