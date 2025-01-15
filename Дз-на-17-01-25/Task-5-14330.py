for N in range(10000, 100000):
    S = (max([int(i) for i in str(N)]) + min([int(i) for i in str(N)])) ** 2
    P = 1
    for i in str(N): P *= int(i) if int(i) % 2 == 0 else 1
    if S > P:
        RES = str(S) + str(P)
    else:
        RES = str(P) + str(S)

    if RES == "12116":
        print(N)
        break

# 22229
