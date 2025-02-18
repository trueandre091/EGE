from itertools import product
from string import digits as d
ans = []
for r in range(4):
    for z in product(d, repeat=r):
        z = ''.join(z)
        for v in d:
            for y in d:
                num = int(f"54{v}1{y}3{z}7")
                if num % 18579 == 0:
                    ans.append((num, num // 18579))

ans = sorted(ans)
for i in ans:
    print(*i)