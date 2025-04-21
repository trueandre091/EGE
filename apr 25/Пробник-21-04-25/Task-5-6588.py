for N in range(1, 100000):
    NN = bin(N)[2:]
    NN = "".join(["0" if i == "1" else "1" for i in NN])
    NN = "1" + NN
    NN += "1" if NN.count("1") % 2 != 0 else "0"
    R = int(NN, 2)
    if R > 180:
        print(N)
        break



