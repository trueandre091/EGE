with open("24-input.txt") as f:
    data = f.readline()

data = data.replace("FSRQ", "*")
data = data.split("*")

max_s = 0
for i in range(len(data)):
    s = "FSRQ".join(data[i:i+81])
    max_s = max(len(s), max_s)

print(max_s + 6)
# 2379
