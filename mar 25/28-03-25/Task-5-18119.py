def f(n):
    res = ""
    while n:
        res = str(n % 3) + res
        n //= 3
    return res

a = []
for N in range(1, 10000):
    NN = f(N)
    summ = sum(map(int, NN))
    if summ % 2 == 0:
        NN = "1" + NN + "2"
    else:
        NN = "2" + NN + "0"
    R = int(NN, 3)
    if R > 100:
        a.append(R)

print(min(a))