from itertools import product
n = 0
for word in product(sorted('ПРИВЫЧКА'), repeat = 5):
    n += 1
    if n % 5 != 0 and len(set(word)) == 5 and all(x not in word for x in 'ИЫА'):
        print(n - n // 5)
        break