from re import *

pattern = r"(?<=ndj)\w{5}"

s = "ndjomedinuvmeodks"

match = search(pattern, s)

print(match.group())



