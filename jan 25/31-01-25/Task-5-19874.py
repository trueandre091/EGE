def f(n):
    res = ""
    while n:
        res = str(n % 3) + res
        n //= 3
    return res

a = []
for N in range(10, 10000):
    NN = f(N)
    if N % 4 == 0:
        NN += NN[-3:]
    else:
        NN = "1" + NN + "20"
    R = int(NN, 3)
    if R > 423:
        a.append(R)

print(min(a))