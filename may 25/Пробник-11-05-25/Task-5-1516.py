a = set()
for N in range(100, 1001):
    NN = bin(N)[2:]
    NN = "".join(NN.split("0"))
    R = int(NN, 2)
    a.add(R)

print(len(a))

# 9

