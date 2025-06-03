with open("26_4629.txt") as f:
    f.readline()
    data = [int(i) for i in f]

pred = []
while data:
    for i in range(3):
        minn = min(data)
        pred.append(minn)
        data.remove(minn)

    maxx = max(data)
    pred.append(maxx)
    data.remove(maxx)

sum_pred = 0
for i in range(len(pred)):
    if (i + 1) % 4 == 0:
        sum_pred += pred[i] // 2
    else:
        sum_pred += pred[i]

print(sum_pred)

###################################

with open("26_4629.txt") as f:
    f.readline()
    data = [int(i) for i in f]

real = []
while data:
    for i in range(3):
        maxx = max(data)
        real.append(maxx)
        data.remove(maxx)

    minn = min(data)
    real.append(minn)
    data.remove(minn)

sum_real = 0
for i in range(len(real)):
    if (i + 1) % 4 == 0:
        sum_real += real[i] // 2
    else:
        sum_real += real[i]

print(sum_real)



