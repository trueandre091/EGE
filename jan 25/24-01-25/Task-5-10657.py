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
    if summ % 3 == 0:
        NN = "20" + NN
    else:
        NN = "10" + NN
    R = int(NN, 3)
    if R < 100:
        a.append(N)

print(max(a))

# 18
