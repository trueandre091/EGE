with open("9_21704.txt") as f:
    data = [list(map(int, i.split())) for i in f]

for row in data:
    if sorted(row, reverse=True) == row:
        S1 = (min(row) + max(row)) / 2
        S2 = (sum(row) - min(row) - max(row)) / 5
        if S1 > S2:
            print(sum(row))
            break



