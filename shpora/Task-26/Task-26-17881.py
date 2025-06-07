with open("26_17881.txt") as f:
    N = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

# data = [
#     [4, 4, 4, 4, 4],
#     [7, 5, 5, 5, 2],
#     [10, 3, 4, 4, 5],
#     [1, 4, 4, 4, 3],
#     [6, 3, 5, 5, 3],
#     [2, 2, 2, 2, 2],
#     [13, 2, 2, 2, 3],
#     [3, 3, 3, 3, 3]
# ]

passed = sorted(
    [st for st in data if 2 not in st[1:]],
    key=lambda x: (-(sum(x[1:]) / 4), x[0])
)
not_passed = sorted(
    [st for st in data if 2 in st[1:]],
    key=lambda x: (x[1:].count(2), x[0])
)

good = passed[:len(data)//4]
print(good[-1])
print([st for st in not_passed if st[1:].count(2) > 2])




