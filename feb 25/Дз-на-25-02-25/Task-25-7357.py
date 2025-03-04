# 1 способ
from itertools import product
from string import digits

ans = []
for r in range(7):
    for p in product(digits, repeat=r):
        p = ''.join(p)
        if p and int(p) % 2 == 0:
            continue
        for k in '2468':
            num = int(f"{k}136{p}")
            if num % 53191 == 0:
                ans.append((num, num // 53191))

ans = sorted(ans)
for i in ans[-5:]:
    print(*i)

print()
# 2 способ
from fnmatch import fnmatch

ans = []
c = 0
for n in range(10**10 - 10**10 % 53191, 0, -53191):
    if c == 5:
        break
    if fnmatch(str(n), "[2468]136*"):
        if int(str(n)[4:]) % 2 != 0:
            if n % 53191 == 0:
                ans.append((n, n//53191))
                c += 1
ans = sorted(ans)
for i in ans:
    print(*i)