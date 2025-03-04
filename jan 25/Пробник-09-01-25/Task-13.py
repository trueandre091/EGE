from ipaddress import *

net = ip_network("101.157.240.0/255.255.252.0", 0)

c = 0
for ip in net:
    if f"{int(ip):032b}"[:16].count("1") > f"{int(ip):032b}"[16:].count("1"):
        c += 1

print(c)
