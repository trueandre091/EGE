a = []
for N in range(1, 1000):
    NN = bin(N)[2:]
    if N % 5 == 0:
        NN = NN[:3] + NN
    else:
        NN += bin(N % 5 * 5)[2:]
    R = int(NN, 2)
    if R < 313 and N % 2 != 0:
        a.append(N)

print(max(a))

# 35