with open("17_4622.txt") as f:
    data = [int(i) for i in f]

minn = min([i for i in data if i > 0 and abs(i) % 19 == 0])

def f(pair):
    if sum(pair) < minn:
        return True
    return False

a = []
for i in range(len(data) - 1):
    pair = data[i:i+2]
    if f(pair):
        a.append(sum(pair))

print(len(a), abs(max(a)))