def c(n):
    res = ""
    while n:
        res = str(n % 3) + res
        n //= 3
    return res

a = []
for N in range(11, 10000):
    NN = c(N)
    if NN.count("0") + NN.count("2") > NN.count("1"):
        NN = "22" + NN
    else:
        NN = "11" + NN
    R = int(NN, 3)
    if R > 100:
        a.append(R)

print(min(a))
