from itertools import product
from string import digits

ans = []
for r in range(4):
    for x in product(digits, repeat=r):
        x = "".join(x)
        for j in digits:
            num = int(f"85{j}16{x}4")
            if num % 2658 == 0:
                ans.append((num, num // 2658))

ans = sorted(ans)
for i in ans:
    print(*i)
    



