with open("24_4643.txt") as f:
    data = f.readline()

data = data.replace("B", "A")
data = data.replace("2", "1")

data = data.replace("11A", "*")

s = 0
for i in range(10000):
    if ("*" * i) in data:
        s = i

print(s)