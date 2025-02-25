# 1 способ
from itertools import product
from string import digits

ans = []
for r in range(3):
    for p in product(digits, repeat=r):
        p = ''.join(p)
        for k in product(digits, repeat=3):
            num = int(f"12{k[0]}3{p}456{k[1]}{k[2]}9")
            if num % 98591 == 0:
                ans.append((num, num // 98591))

ans = sorted(ans)
for i in ans:
    print(*i)

print()
# 2 способ
from fnmatch import fnmatch
for n in range(1203456009 - 1203456009 % 98591, 13 * 10**10, 98591):
    if fnmatch(str(n), "12?3*456??9"):
        print(n, n // 98591)