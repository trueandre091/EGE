c = 0
for N in range(1, 1000000):
    NN = hex(N)[2:]
    if NN.count("b") % 2 == 0:
        NN = "1" + NN
    else:
        NN += "1"
    R = int(NN, 16)
    if 10 <= abs(R) <= 99:
        c += 1

print(c)

