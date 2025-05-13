with open("24_3584.txt") as f:
    data = f.readline()

data = data.replace("BA", "*").replace("DA", "*")

for i in "ABD":
    data = data.replace(i, " ")

data = data.split()

print(len(max(data,key=len)))


