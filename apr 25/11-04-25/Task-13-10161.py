from ipaddress import *

ip1 = ip_address("211.115.61.154")
ip2 = ip_address("211.115.59.137")

ip1 = f"{int(ip1):032b}"
ip2 = f"{int(ip2):032b}"

print(ip1)
print(ip2)

