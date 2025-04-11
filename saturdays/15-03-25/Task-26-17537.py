with open("26_17537.txt") as f:
    N, M, K = list(map(int, f.readline().split()))
    seats = [list(map(int, i.split())) for i in f]

seats = sorted(seats, key=lambda x: (x[1], -x[0]))
booked = [M + 1] * (K + 1)

for seat in seats:
    booked[seat[1]] = seat[0]

ans = []
for i in range(1, K):
    r1, r2 = booked[i:i + 2]
    ans.append((min(r1, r2) - 1, i + 1))

ans = sorted(ans, key=lambda x: (-x[0], -x[1]))
print(ans[0])




