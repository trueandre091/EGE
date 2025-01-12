from ipaddress import ip_network, ip_address

ip = "218.194.82.148"
mask = "255.255.255.192"

net = ip_network(f"{ip}/{mask}", 0)

a = []
for ad in net:
    a.append(ad)

print(a[-2])