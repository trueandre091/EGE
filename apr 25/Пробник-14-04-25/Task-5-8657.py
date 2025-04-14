def f(n):
    res = ""
    while n:
        res = str(n % 3) + res
        n //= 3
    return res

for N in range(1, 100000):
    NN = f(N)
    if N % 5 == 0:
        NN += NN[-3:]
    else:
        NN += f(N % 5 * 5)
    R = int(NN, 3)
    if R < 5496:
        print(N)
