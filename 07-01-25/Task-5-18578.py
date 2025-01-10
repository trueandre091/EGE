def c(N):
    NN = ""
    while N:
        NN = str(N % 4) + NN
        N //= 4
    return NN

for N in range(1, 100000):
    NN = c(N)
    if N % 4 == 0:
        NN = "2" + NN + "03"
    else:
        NN += c((N % 4) * 5)
    R = int(NN, 4)
    if R <= 567:
        print(N)
