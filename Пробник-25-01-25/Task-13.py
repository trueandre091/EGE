from ipaddress import ip_network, ip_address

ip = "203.155.64.98"
net = "203.155.64.0"

ipa = ip_address(ip)

for mask in range(1, 33):
    netw = ip_network(f"{net}/{mask}", strict=0)
    if ipa in netw:
        print(mask)








