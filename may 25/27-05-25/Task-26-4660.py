with open("26_4660.txt") as file:
    n = file.readline()
    costs = [int(i) for i in file]

costs = sorted(costs)[::-1]
mag = sum(costs) - sum(costs[3::4]) // 2
pok = sum(costs[:-int(n) // 4]) + sum(costs[-int(n) // 4:]) // 2

print(mag, pok)




