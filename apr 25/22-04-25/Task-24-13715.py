with open("24_13715.txt") as f:
    data = f.readline()

data = data.split("AB")

a = []
for i in range(len(data) - 50):
    s = "".join(data[i:i+51])
    a.append(len(s) + 100)

print(max(a) + 2)


