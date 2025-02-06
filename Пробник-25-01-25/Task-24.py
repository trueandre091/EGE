with open("24-input.txt") as f:
    data = f.readline()

data = data.replace("N", "*").replace("O", "*").replace("P", "*")

for i in range(100):
    data = data.replace("**", "* *")

data = data.split()
print(len(max(data, key=len)), max(data, key=len))

