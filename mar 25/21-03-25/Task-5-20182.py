def f(n):
    res = ""
    while n:
        res = str(n % 3) + res
        n //= 3
    return res

for N in range(1, 10000):
    NN = f(N)
    if sum(map(int, NN)) % 2 == 0:
        NN = "12" + NN[2:] + "0"
    else:
        NN = "10" + NN[2:] + "2"
    R = int(NN, 3)
    if R > 105:
        print(N)
        break

