from ipaddress import *

def c(i):
    ip = f"{int(i):032b}"
    return ip.count("1") > 15

for A in range(256):
    net = ip_network(f"192.214.{A}.184/255.255.255.224", False)
    if all(c(i) for i in net):
        print(A)
        break


