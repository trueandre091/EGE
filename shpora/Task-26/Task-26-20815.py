with open("26_20815.txt") as f:
    N, K = map(int, f.readline().split())
    data = [list(map(int, i.split())) for i in f]

# K = 4
# data = [
#     [4, 80, 80, 80, 0],
#     [7, 50, 80, 100, 10],
#     [11, 80, 80, 70, 10],
#     [10, 100, 100, 100, 2],
#     [6, 90, 90, 90, 9],
#     [2, 70, 80, 80, 8]
# ]
ab = []
for i in data:
    ab.append(i + [sum(i[1:])])

ab.sort(key=lambda x: (-x[5], -x[4], x[0]))
# print(ab[:K])
# print()
# print(ab[K:K+15])

if ab[K - 1][5] == ab[K][5]:
    pass_score = [i[0] for i in ab if i[5] > ab[K - 1][5]][-1]
    semipass_c = len([i for i in ab if i[5] == ab[K - 1][5]])
    print(pass_score, semipass_c)



