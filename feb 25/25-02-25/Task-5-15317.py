for N in range(1, 1000000):
    NN = bin(N)[2:]
    if N % 2 == 0:
        NN += "01"
    else:
        NN = "1" + NN + "1"

    R = int(NN, 2)
    if R > 156:
        print(N)
        break
