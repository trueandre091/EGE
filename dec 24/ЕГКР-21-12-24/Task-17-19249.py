with open("17-input.txt") as f:
    data = [int(i) for i in f]

ans = []
for i in range(len(data) - 2):
    a1, a2, a3 = data[i], data[i+1], data[i+2]
    k1 = [i for i in [a1, a2, a3] if len(str(abs(i))) == 5 and str(abs(i))[-2:] == "43"]
    if not k1:
        continue
    max_k1 = max(k1)
    sum_sq = sum([i**2 for i in [a1, a2, a3] if i != max_k1])
    if sum_sq <= max_k1**2:
        ans.append(sum([i**2 for i in [a1, a2, a3]]))

print(len(ans), min(ans))
# 76 838850571 первое числоневерно
