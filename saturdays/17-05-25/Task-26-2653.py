with open("26_2653.txt") as f:
    f.readline()
    data = [int(i) for i in f]

from itertools import combinations

summ = sum(data)
data = sorted(data, reversed=True)
end = False

ans = []

for n in range(summ, 1, -1):
    nice = False
    l, r = 0, len(data)
    cur = summ
    while cur != n:
        cur = sum(data[l:r])
        if cur > n:
            r -= 1
        if cur < n:
            l += 1



print(len(ans))







