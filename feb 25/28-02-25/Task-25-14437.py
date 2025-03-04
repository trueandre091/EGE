def f(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: res |= {i, n //i}
    return res

c = 0
for n in range(0, 700000)[::-1]:
    k = f(n)
    if k:
        M = sum(k) // len(k)
    else:
        M = 0
    if M < 313:
        continue
    if str(M)[-3:] == "313":
        print(n, M)
        c += 1
    if c == 7:
        break


