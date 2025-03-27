def f(x):
    res = ""
    while x:
        res = str(x % 4) + res
        x //= 4
    return res

a = []
for N in range(1, 10000):
    NN = f(N)
    summ = sum(map(int, NN))
    if summ % 2 == 0:
        NN += NN[-2:]
    else:
        NN = "2" + NN + "0"
    R = int(NN, 4)
    if (R > 120) and (R % 2 == 0):
        a.append(R)

print(min(a))

