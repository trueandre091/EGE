from fnmatch import fnmatch
from itertools import product
from string import digits

ch = digits[::2]
nech = digits[1::2]

ans = []
for r in range(4):
    for bob in product(nech, repeat=r):
        bob = "".join(bob)
        for A in ch:
            num = int(f"1{A}2157{bob}4")
            if num % 133 == 0 and num <= 10**10:
                ans.append((num, num//133))

ans = sorted(ans)
for i in ans:
    print(*i)



