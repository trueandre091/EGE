from itertools import product

alph = sorted(set("ЯНВАРЬ"))

for pos, word in enumerate(product(alph, repeat=5), 1):
  word = "".join(word)
  if word[0] != "Я" and word.count("Ь") <= 1 and "ЯЯ" not in word:
    print(pos, word)


# 6406
