with open("24_3228.txt") as f:
    data = f.readline()

data = data.replace("AC", "*")
data = data.replace("AB", "*")

for i in "ABC":
    data = data.replace(i, " ")

data = data.split()

print(len(max(data, key=len)))