with open("17_17558.txt") as f:
    data = [int(i) for i in f]

lenn = len([i for i in data if abs(i) % 32 == 0])

def f(pair):
    if (pair[0] < 0) or (pair[1] < 0):
        return True
    return False

def f1(pair):
    if sum(pair) < lenn:
        return True
    return False

a = []
for i in range(len(data) - 1):
    pair = data[i:i+2]
    if f(pair) and f1(pair):
        a.append(sum(pair))

print(len(a), max(a))

