a = []
for N in range(1, 100000):
    NN = bin(N)[2:]
    NN += str(NN.count("1") % 2)
    NN += str(NN.count("1") % 2)
    R = int(NN, 2)
    if R > 75:
        a.append(R)

print(min(a))


