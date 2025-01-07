for N in range(1, 10000):
    NN = oct(N)[2:]
    if N % 2 == 0:
        NN += str(max(map(int, NN)))
    else:
        NN += oct(min(map(int, NN)) * 2)[2:]
    R = int(NN, 8)
    if R < 313:
        print(N)
