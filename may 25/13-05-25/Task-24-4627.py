with open("24_4627.txt") as f:
    data = f.readline()

data = data.replace("NPO", "*").replace("PNO", "*")
for i in "PNO":
    data = data.replace(i, " ")

data = data.split()

print(len(max(data, key=len)))

