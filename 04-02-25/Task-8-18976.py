from itertools import product
from string import digits , ascii_lowercase

alph = digits + ascii_lowercase

ch = alph[::2]
nech = alph[1::2]

c = 0
for i in product(alph[:20], repeat=5):
    if i[0] == "0":
        continue

    sum1 = int(i[0], 36) + int(i[-1], 36)
    if sum1 == 26:
        f = False
        if i[0] in ch:
            for k in range(1, len(i)):
                if k % 2 != 0:
                    if i[k] not in nech:
                        break
                else:
                    if i[k] not in ch:
                        break
            else:
                f = True
                print([int(l, 36) for l in i])
        else:
            for k in range(1, len(i)):
                if k % 2 != 0:
                    if i[k] not in ch:
                        break
                else:
                    if i[k] not in nech:
                        break
            else:
                f = True

        if f:
            c += 1
            print([int(l, 36) for l in i])

print(c)





