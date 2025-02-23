from ipaddress import ip_address, ip_network

net = ip_network("101.157.240.0/255.255.252.0", strict=0)

c = 0
for ip in net:
    ip = f"{ip:b}"
    ip12 = ip[:16]
    ip34 = ip[16:]
    if ip12.count("1") > ip34.count("1"):
        c += 1
print(c)

