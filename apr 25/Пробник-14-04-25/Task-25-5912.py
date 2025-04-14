from fnmatch import fnmatch

def f(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: res |= {i, n//i}
    return res

for n in range(10**7 + 1):
    if fnmatch(str(n), "12?*45"):
        d = f(n)
        if len(d) == 18:
            print(n, max(d))


