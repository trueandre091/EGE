with open("24-7979.txt") as f:
    data = f.readline()

from re import *

def eval_8(s):
    nums = split(r"[+*]", s)
    oper = split(r"[0-9]+", s)[1:-1]
    res = ""
    for i in range(len(nums)):
        res += str(int(nums[i], 8))
        if i != (len(nums) - 1):
            res += oper[i]
    return eval(res)

num = r"([1-7][0-7]*|0)"
pattern = rf"(?<=F){num}([+*]{num})+"

matches = [i.group() for i in finditer(pattern, data)]

matches = sorted(matches, key=len)

ans = []
for i in matches:
    res = eval_8(i)
    ans.append((res, i))

ans = sorted(ans, key=lambda x: (len(x[1]), x[0]))

print(ans[-1])




