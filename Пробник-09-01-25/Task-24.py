with open("24-input.txt") as f:
    data = f.readline()

C = data.count("A")
N = sum(range(C))
CC = sum([1 for i in range(len(data) - 1) if data[i] + data[i + 1] == "AA"])
RES = N - CC
print(RES)
