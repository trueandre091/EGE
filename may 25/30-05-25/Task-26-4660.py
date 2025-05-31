with open("26_4660.txt") as f:
    N = int(f.readline())
    data = [int(i) for i in f]

data = sorted(data)
shop = sum(data) - sum(data[:N//4]) // 2

data = sorted(data, reverse=True)
pokupatel = sum(data) - sum(data[3::4]) // 2

print(pokupatel, shop)





