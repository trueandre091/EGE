with open("26-input.txt") as f:
    f.readline()
    data = [list(map(int, i.split())) for i in f]

N = 100
strategy = []

def check(data):
    r = [i[0] for i in data]
    if N >= min(r):
        return True
    return False

while check(data):
    able = [lvl for lvl in data if lvl[0] <= N]
    able = sorted(able, key=lambda x: -x[1])
    if able[0] not in strategy:
        strategy.append(able[0])
    data.remove(able[0])
    N += able[0][1]

print(strategy, len(strategy), N)
        
