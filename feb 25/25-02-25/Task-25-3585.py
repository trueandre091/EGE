from itertools import product
from string import digits

ans = []
for k in product(digits, repeat=2):
    num = int(f"1234{k[0]}57{k[1]}8")
    if num % 17 == 0 and num <= 10**9:
        ans.append((num, num // 17))

ans = sorted(ans)
[print(*i) for i in ans]

