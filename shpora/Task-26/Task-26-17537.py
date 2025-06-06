with open("26_17537.txt") as f:
    N, M, K = map(int, f.readline().split())
    data = [list(map(int, i.split())) for i in f]

rows = []
for i in range(K):
    i_s = [s[0] for s in data if s[1] == i]
    if i_s:
        rows.append(min(i_s) - 1)
    else:
        rows.append(M)


ans = []
for i in zip(rows, rows[1:]):
    ans.append(min(i))

print(max(ans), K - (ans[::-1].index(max(ans)) + 1))
# +1 потому что индексы считаются с нуля





