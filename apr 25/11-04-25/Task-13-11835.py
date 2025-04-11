from ipaddress import *

def check(i):
    ip = f"{int(i):032b}"
    return ip[:16].count("0") > ip[16:].count("0")

c = 0
for A in range(256):
    net = ip_network(f"207.0.{A}.167/255.255.255.192", False)
    if all(check(i) for i in net):
        c += 1

print(c)

