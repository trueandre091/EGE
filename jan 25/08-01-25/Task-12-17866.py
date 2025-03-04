s = 81 * "1"

while "11111" in s or "888" in s:
    if "11111" in s:
        s = s.replace("11111", "88", 1)
    else:
        s = s.replace("888", "8", 1)

print(s)