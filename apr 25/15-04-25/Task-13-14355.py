from ipaddress import *

def f(i):
    ip = f"{int(i):032b}"
    return ip[:16].count("1") >= ip[16:].count("1")

for A in range(16, 25):
    net = ip_network(f"127.63.67.1/{A}", 0)
    if all(f(i) for i in net):
        print(A)
        break


