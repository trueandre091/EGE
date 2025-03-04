with open("17_9748.txt") as f:
    data = [int(i) for i in f]

maxx = max([i for i in data if str(i)[-2:] == "15"])

def f(pair):
    if (1000 <= pair[0] <= 9999) + (1000 <= pair[1] <= 9999) + (1000 <= pair[2] <= 9999) == 1:
        return True
    return False

a = []
for i in range(len(data) - 2):
    pair = data[i:i+3]
    if f(pair):
        if sum(pair) >= maxx:
            a.append(sum(pair))

print(len(a), max(a))
