# 1 способ
from itertools import product
from string import digits

k = [111, 113, 127]
ans = []
for r in product([0, 1, 2], repeat=2):
    if sum(r) > 2:
        continue
    for p1 in product("123456789", repeat=r[0]):
        for p2 in product(digits, repeat=r[1]):
            p1, p2 = "".join(p1), "".join(p2)
            num = int(f"{p1}15{p2}7424")
            h = [num % i == 0 for i in k]
            if any(h):
                ans.append((num, num // k[h.index(True)]))

ans = sorted(ans)
for i in ans:
    print(*i)

