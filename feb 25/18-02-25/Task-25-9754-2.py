from itertools import product
from string import digits

ans = []

for r in range(4):
    for z in product(digits, repeat=r):
        z = "".join(z)
        for v in digits:
            num = int(f"3{v}1{z}57")
            if num % 2023 == 0:
                ans.append((num, num // 2023))

ans = sorted(ans)
for i in ans:
    print(*i)