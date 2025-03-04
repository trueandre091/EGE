# 1 способ
from itertools import product
from string import digits

ans = []
for r in range(4):
    for p in product(digits, repeat=r):
        p = "".join(p)
        for k in digits:
            num = int(f"1{k}2139{p}4")
            if num % 3052 == 0:
                ans.append((num, num // 3052))

ans = sorted(ans)
for i in ans:
    print(*i)


print()
# 2 способ
from fnmatch import fnmatch

for n in range(3052, 10**10, 3052):
    if fnmatch(str(n), "1?2139*4"):
        print(n, n // 3052)



