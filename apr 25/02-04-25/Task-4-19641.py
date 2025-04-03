from itertools import product, permutations, combinations

def count(d):
    return sum([len(d[letter]) for letter in word])

def fano(d):
    codes = d.values()
    for x in codes:
        if any(x.startswith(y) or y.startswith(x) for y in codes if x != y):
            return False
    if len(codes) != len(set(codes)):
        return False
    return True

alph = "СВЕТИЛО"
word = alph
used = {"С": "11", "В": "01" , "Е": "101", "Т": "1000", "И": "00"}
tree = [''.join(i) for r in range(1, 7) for i in product("01", repeat=r)]

a = []
for p in permutations("ЛО"):
    for codes in combinations(tree, len(p)):
        need = dict(zip(p, codes))
        d = {**used, **need}
        if fano(d): a.append((count(d), d))

print(min(a, key=lambda x: x[0]))






