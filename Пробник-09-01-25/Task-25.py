from fnmatch import fnmatch

c = 0
m = []
for n in range(596, 10**12, 596):
    if str(n)[0] != "1":
        continue
    if str(n)[-2:] != "64":
        continue
    if "28" not in str(n):
        continue
    if fnmatch(str(n), "1*28?64"):
        c += 1
        m.append(n)

print(c, sum(m)//c)
