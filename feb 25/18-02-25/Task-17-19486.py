with open("17_19486.txt") as f:
    data = [int(i) for i in f]

count = len([i for i in data if str(i)[-1] == "7"])

def f(pair):
    if pair[0] * pair[1] < 0:
        if sum(pair) < count:
            return True

    return False

ans = []

for i in range(len(data) - 1):
    pair = data[i:i+2]
    if f(pair):
        ans.append(sum(pair))

print(len(ans), max(ans))


