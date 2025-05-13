with open("24_1975.txt") as f:
    data = f.readline()

while "PP" in data:
    data = data.replace("PP", "P P")
data = data.split()

print(len(max(data, key=len)))

