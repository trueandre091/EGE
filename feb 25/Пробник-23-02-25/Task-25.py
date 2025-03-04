from fnmatch import fnmatch


def dels(n):
    res = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            res.add(i)
            res.add(n // i)
    return res

for x in range(7777, 10**10, 7777):
    if fnmatch(str(x), "12*567?"):
        dells = dels(x)
        if (min(dells) + max(dells)) % 2 != 0:
            if x % 7777 == 0:
                print(x, x//7777)

# 121025674 15562
# 1209805674 155562
# 1220895676 156988
# 1231985678 158414
# 1265395670 162710
# 1276485672 164136
# 1287575674 165562
# 1298665676 166988

