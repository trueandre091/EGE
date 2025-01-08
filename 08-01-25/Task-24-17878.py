with open("24_input.txt") as f:
    data = f.readline()

data = data.replace("-", "*")
data = data.replace("**", " ").replace(" *", " ").replace("* ", " ")
data = data.replace("7", "6").replace("8", "6").replace("9", "6")

for i in range(1, 100):
    data = data.replace(f"*{'0' * i}6", " 6")
    data = data.replace(f" {'0' * i}6", " 6")

data = data.split()

print(len(max(data, key=len)))

# 154
