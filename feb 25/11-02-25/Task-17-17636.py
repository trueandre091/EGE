with open("17_17636.txt") as f:
    data = [int(i) for i in f]

maxx = max(i for i in data if (str(i)[-1:] == "3") and (100 <= abs(i) <= 999))











