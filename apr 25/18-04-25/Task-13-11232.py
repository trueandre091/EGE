from ipaddress import *

net = ip_network(f"192.168.31.80/255.255.255.240", 0)

a = []

for i in net:
    ip = f"{int(i):032b}"
    a.append(ip.count("1"))

print(max(a))

