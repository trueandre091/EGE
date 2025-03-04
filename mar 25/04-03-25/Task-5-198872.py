def f(n):
    res = ""
    while n:
        res = str(n % 7) + res
        n //= 7
    return res

a = []
for N in range(1, 10000):
    NN = f(N)
    if N % 2 == 0:
        NN = "52" + NN + "1"
    else:
        NN = NN[-1] + NN[1:-1] + NN[0] + "15"

    while NN[0] == "0":
        NN = NN[1:]

    if len(NN) == 4 and N <= 1000:
        a.append(N)

print(max(a))














