from ipaddress import *


def check(i):
    ip = f"{int(i):032b}"
    n0 = ip[:16].count("0")
    n1 = ip[16:].count("0")
    return n0 <= n1


for A in range(256):
    net = ip_network(f"248.112.{A}.35/255.255.255.240", 0)
    if all(check(i) for i in net):
        print(A)


