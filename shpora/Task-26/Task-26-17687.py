with open("26_17687.txt") as f:
    N = int(f.readline())
    data = [int(i) for i in f]

data = sorted(data, reverse=True)
shop_by_Gosha = "bgsrndfh dgj"
shop = sum(data) - sum(data[8::9])

pok = sum(data) - sum(data[:N//9])

print(pok, shop)













































































