with open("17_4597.txt") as f:
    data = [int(i) for i in f]

minn = min(data)

def check(pair):
    if pair[0] % 117 == minn or pair[1] % 117 == minn:
        return True
    return False

a = []
for i in range(len(data) - 1):
    pair = data[i:i+2]
    if check(pair):
        a.append(sum(pair))

print(len(a), max(a))




























