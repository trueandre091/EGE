def f(n):
    res = ""
    while n:
        res = str(n % 3) + res
        n //= 3
    return res

a = []
for N in range(1, 10000):
    NN = f(N)
    if N % 3 == 0:
        NN = "1" + NN + "02"
    else:
        NN += f(N % 3 * 4)
    R = int(NN, 3)
    if R < 199:
        a.append(N)

print(max(a))
