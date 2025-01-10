a = []
for N in range(1, 10000):
    NN = bin(N)[2:]
    if N % 2 == 0:
        NN = "10" + NN
    else:
        NN = "1" + NN + "01"
    R = int(NN, 2)
    if N <= 12:
        a.append(R)

print(max(a))

# 109