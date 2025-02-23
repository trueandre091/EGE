with open("27-B-input.txt") as f:
    data = [int(i) for i in f]

N = 4000000
K = 200000
T = 500000

lis = []
max_sum = (-1, -1)
for i in range(len(data) - K):
    if i - max_sum[1] < T:
        continue
    r = data[i:i+K]
    summ = sum(r)
    if summ > max_sum[0]:
        max_sum = (summ, i)
    lis.append((i, summ))


lis = sorted(lis, key=lambda x: -x[1])
[print(*i) for i in lis[:5]]




