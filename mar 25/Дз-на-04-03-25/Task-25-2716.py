def f(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: res |= {i, n//i}
    return res

c = 0
for n in range(1090000, 1200000):
    d = sorted(f(n))
    if len(d) >= 3:
        S = sum(d[-3:])
    else:
        S = 0
    if S != 0 and S % 2022 == 0 and S != n:
        print(n, S)
        c +=1
    if c == 5:
         break

# 1091880 1182870
# 1116144 1209156
# 1140408 1235442
# 1164672 1261728
# 1188936 1288014
