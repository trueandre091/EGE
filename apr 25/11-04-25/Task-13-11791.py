from ipaddress import *


def check(ip):
    ip = f"{int(ip):032b}"
    return ip[:16].count("0") <= ip[16:].count("0")


for A in range(33):
    net = ip_network(f"246.51.128.202/{A}", strict=False)
    if all(check(i) for i in net):
        print(A)


