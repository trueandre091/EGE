with open("9-9778.txt") as f:
    data = [list(map(int, i.split())) for i in f]


for i in range(len(data)):
    row = data[i]
    cs = [row.count(j) for j in row]
    if cs.count(2) == 2 and cs.count(1) == 4:
        pov = [j for j in row if row.count(j) == 2][0]
        nepov = [j for j in row if j != pov]
        if pov >= (sum(nepov) / 4):
            print(i + 1)
            break
