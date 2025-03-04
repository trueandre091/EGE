from ipaddress import ip_address, ip_network

net = ip_network("222.121.128.0/255.255.224.0", 0)

a = 0
for ip in net:
    if f"{ip:b}"[-1] == f"{ip:b}"[-2]:
        a += 1

print(a)