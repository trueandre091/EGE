s = "1" * 81
while "111" in s or "88888" in s:
    if "111" in s:
        s = s.replace("111", "88", 1)
    else:
        s = s.replace("88888", "8", 1)
print(s)