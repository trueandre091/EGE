from itertools import product
from string import digits

ans = []

for r in range(3):
    for z in product(digits, repeat=r):
        z = "".join(z)
        for x in digits:
            for y in digits:
                num = int(f"3{x}12{y}14{z}5")
                if num % 1917 == 0:
                    ans.append((num, num // 1917))

ans = sorted(ans)
for i in ans:
    print(*i)

