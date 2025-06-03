a = []
for N in range(1, 10000):
    NN = bin(N)[2:]
    if N % 3 == 0:
        NN += NN[-3:]
    else:
        NN += bin(N % 3 * 3)[2:]
    R = int(NN, 2)
    if R <= 170:
        a.append(R)

print(max(a))