from itertools import product
from string import digits as d

ans = []
for r in range(3):
    for z in product(d, repeat=r):
        z = "".join(z)
        for v in d:
            for y in d:
                num = int(f"1{z}2{v}{y}76")
                if num % 1923 == 0:
                    ans.append((num, num//1923))

ans = sorted(ans)
for i in ans:
    print(*i)