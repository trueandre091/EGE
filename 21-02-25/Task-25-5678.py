from fnmatch import fnmatch

for n in range(124579 - 124579 % (1 + 5 + 7 + 9), 125 * 10**5):
    k = sum([int(i) for i in str(n) if int(i) % 2 != 0])
    if k == 0:
        continue
    if n % k == 0:
        if fnmatch(str(n), "124*5*79"):
            print(n, sum(map(int, str(n))))

