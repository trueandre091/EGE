from itertools import product

ans = set()
for i in range(69):
    itog = (-2) * i + 3 * (69 - i)
    ans.add(itog)

print(len(ans))



