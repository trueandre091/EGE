from ipaddress import *

def check(ip):
    ip = f"{int(ip):032b}"
    if ip[:16].count("0") >= ip[16:].count("0"):
        return True
    return False

for A in range(33):
    net = ip_network(f"152.65.245.132/{A}", strict=False)
    if all(check(ip) for ip in net):
        print(A)

