from ipaddress import ip_network, ip_address

net = ip_network("172.16.128.0/255.255.192.0", strict=False)

c = 0
for i in net:
    ip = f"{int(i):032b}"
    if ip.count("1") % 2 != 0:
        c += 1

print(c)