# 1 способ
from itertools import product
from string import digits

ans = []
for r in range(4):
    for p in product('0123456', repeat=r):
        p = ''.join(p)
        for k in '123456':
            num = int(f"{k}213{p}5664", 7)
            if num % 333 == 0 and num <= 10**9:
                ans.append((num, num // 333))

ans = sorted(ans)
[print(*i) for i in ans]

print()
# 2 способ
from fnmatch import fnmatch

def f(n):
    res = ''
    while n:
        res = str(n % 7) + res
        n //= 7
    return res

for n in range(333, 10**9, 333):
    n7 = f(n)
    if fnmatch(n7, '?213*5664'):
        print(n, n // 333)

