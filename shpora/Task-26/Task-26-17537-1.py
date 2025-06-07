with open("26_17537.txt") as f:
    N, M, K = map(int, f.readline().split())
    data = [list(map(int, i.split())) for i in f]

seats = []
for seat in range(K):
    rows = [i[0] for i in data if i[1] == seat]
    if rows:
        seats.append(min(rows) - 1)
    else:
        seats.append(M)

ans = []
for i in range(K - 1):
    ans.append(min(seats[i], seats[i + 1]))

print(max(ans), K - (ans[::-1].index(max(ans)) + 1))




