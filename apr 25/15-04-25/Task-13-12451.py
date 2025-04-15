from ipaddress import *

def f(i):
    ip = f"{int(i):032b}"
    return ip[16:24].count("0") > ip[24:].count("0")

c = 0
for A in range(256):
    if f"{A:08b}".count("0") < 5:
        c += 1
    # net = ip_network(f"246.81.65.{A}/255.255.255.224", 0)
    # net = list(net)[1:-1]
    # if all(f(i) for i in net):
    #     c += 1

print(c)
