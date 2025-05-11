with open("24_14502.txt") as f:
    data = f.readline().strip()

from string import *
from itertools import *

alph = set(ascii_uppercase)
char_count = {k: 0 for k in alph}
window_chars = set()
min_len = 10**20
left = 0

for right in range(len(data)):
    char = data[right]
    char_count[char] += 1
    window_chars.add(char)

    while window_chars == alph:
        min_len = min(min_len, right - left + 1)
        left_char = data[left]
        char_count[left_char] -= 1
        if char_count[left_char] == 0:
            window_chars.remove(left_char)
        left += 1

print(min_len)

