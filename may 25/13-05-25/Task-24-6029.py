with open("24_6029.txt") as f:
    data = f.readline()

while "EE" in data:
    data = data.replace("EE", "E E")
while "FF" in data:
    data = data.replace("FF", "F F")

data = data.replace("D", " ")

data = data.split()
print(len(max(data, key=len)))


