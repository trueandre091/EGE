with open("26_4684.txt") as f:
    N = int(f.readline())
    data = [int(i) for i in f]

data = sorted(data, reverse=True)
pokupatel = sum(data) - sum(data[5::6]) // 2

data = sorted(data)
shop = sum(data) - sum(data[:N//6]) // 2

print(pokupatel, shop)




