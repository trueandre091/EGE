for N in range(2, 1000000):
    NN = bin(N)[2:]
    c1, c0 = 0, 0
    for i in range(len(NN)):
        if i % 2 != 0:
            if NN[i] == "1": c1 += 1
        else:
            if NN[i] == "0": c0 += 1
    R = abs(c1 - c0)
    if R == 5:
        print(N)
        break
