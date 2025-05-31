with open("26_6759.txt") as f:
    N = int(f.readline())
    data = [int(i) for i in f]

data = sorted(data, reverse=True)
pok = sum(data) - sum(data[:N//3])
shop = sum(data) - sum(data[2::3])
print(pok, shop)





