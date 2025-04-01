from itertools import product, permutations

alph = "ЕИМТОРЯ"
word = "ТЕРРИТОРИЯ"

def count(d):
    return [int(d[letter], 2) for letter in word]

def fano(d):
    for value in d.values():
        if any(value.startswith(x) or x.startswith(value) for x in d.values()):
            return False
    return True

used = "ЕИОЯ"
need = set(alph) - set(used)
tree = [''.join(i) for r in range(1, 6) for i in product("01", repeat=r)]

a = []
for p in permutations(need):
    d = {"Е": "01", "И": "001" , "О": "0001", "Я": "101"}
    d = {**d, **dict(zip(p, tree[:len(p)]))}
    if not fano(d):
        continue
    a.append(count(d))

print(min(a))






