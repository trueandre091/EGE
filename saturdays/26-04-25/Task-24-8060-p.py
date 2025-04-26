with open("24-8060.txt") as f:
    data = f.readline()

from re import *
from string import *


# while ".." in data or "@@" in data:
#     data = data.replace("@@", " ")
#     data = data.replace("..", ". .")


# for i in ascii_uppercase + ascii_lowercase + ".":
#     if i in "yg":
#         continue
#     data = data.replace(f"@{i}", f" {i}")


server = r"(yandex\.ru|gmail\.com)"
pattern = rf"\.?\w+(\.\w+)*@{server}"

matches = [i.group() for i in finditer(pattern, data)]

print(len(max(matches, key=len)))



