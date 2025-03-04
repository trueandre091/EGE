with open("24-input.txt") as f:
    data = f.readline()

data = data.replace("FSRQ", "*")
data = data.split("*")

max_s = ""
for i in range(len(data)):
    s = data[i:i+81]
    summ = sum([len(i) for i in s]) + 4 * (len(s) - 1)
    if summ > len(max_s):
        max_s = "FSRQ".join(s)

print(len(max_s) + 6)
# 2379
