from itertools import product
from string import digits

ans = []
for r in range(1, 7):
    for p in product(digits, repeat=r):
        p = ''.join(p)
        num = int(f"1234{p}")
        if num % 137 == 0 and int(p) % (sum(map(int, p))**3) == 0:
            if num <= 10**10:
                ans.append(num)
ans = sorted(ans)
[print(i) for i in ans]
