from itertools import product
from string import digits as d

ans = []
for r in range(3):
    for z in product(d, repeat=r):
        z = ''.join(z)
        for v in d:
            num = int(f"12{z}34{v}5")
            if num % 2025 == 0:
                ans.append((num, num // 2025))

ans = sorted(ans)
for i in ans:
    print(*i)