a = []
for N in range(1, 100000):
    NN = bin(N)[2:]
    if NN.count("1") % 2 == 0:
        NN = "10" + NN[2:] + "0"
    else:
        NN = "11" + NN[2:] + "1"
    R = int(NN, 2)
    if R > 50:
        print(N)
        break

