from itertools import product
from string import digits

ans = []

for r in range(3):
    for z in product(digits, repeat=r):
        z = "".join(z)
        for y in digits:
            num = int("12" + z + "4" + y + "65")
            if num % 161 == 0:
                ans.append((num, num // 161))


ans = sorted(ans)
for i in ans:
    print(i[0], i[1])



