# 1 способ
from itertools import product
from string import digits

ans = []
for r in range(6):
    for p in product("02468", repeat=r):
        p = "".join(p)
        if p and p[0] == "0":
            continue
        for k in product("13579", repeat=2):
            num = int(f"{p}12{k[0]}4{k[1]}")
            if num % 9231 == 0:
                ans.append((num, num // 9231))

ans = sorted(ans)
for i in ans:
    print(*i)

print()
# 2 способ
from fnmatch import fnmatch
for n in range(9231, 10**10, 9231):
    for r in range(1, 6):
        if fnmatch(str(n), f"{'[02468]' * r}12[13579]4[13579]"):
            print(n, n//9231)
