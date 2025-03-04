def f(n):
    res = ""
    while n:
        res = str(n % 4) + res
        n //= 4
    return res

for N in range(1, 100000):
    NN = f(N)
    if len(NN) % 2 == 0:
        NN = NN[:len(NN)//2] + "0" + NN[len(NN)//2:]
    R = int(NN)
    if R <= 180:
        print(N)

