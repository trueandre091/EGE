from ipaddress import *

def check(ip):
    ip = f"{int(ip):032b}"
    if ip[:16].count("0") <= ip[16:].count("0"):
        return True
    return False

for A in range(256):
    net = ip_network(f"223.167.{A}.167/255.255.255.192", strict=False)
    if all(check(ip) for ip in net):
        print(A)




