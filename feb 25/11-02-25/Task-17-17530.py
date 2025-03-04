with open("17_17530.txt") as f:
    data = [int(i) for i in f]

minn = min(i for i in data)

def f(pair):
    if (pair[0] % 55 == minn) or (pair[1] % 55 == minn):
        return True
    return False

a = []
for i in range(len(data) - 1):
    pair = data[i:i+2]
    if f(pair):
        a.append(sum(pair))

print(len(a), min(a))




