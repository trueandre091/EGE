with open("17_5882.txt") as f:
    data = [int(i) for i in f]

min_elements = []
for p in zip(data, data[1:]):
    if sum(str(i)[-1] == "3" for i in p) == 1:
        min_elements.append(min(p))


summ = sum(map(lambda x: int(x)**2, str(abs(min(min_elements)))))

ans = [i for i in data if ("3" in str(i)) and (i >= summ)]

print(len(ans), min(ans))

