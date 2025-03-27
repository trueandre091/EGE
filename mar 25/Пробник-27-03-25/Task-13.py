from ipaddress import *

ip = ip_address("192.168.24.112")
# ip = f"{ip:b}"
net = "192.168.24.64"
# n = ""
# for i in net.split("."):
#     n += bin(int(i))[2:].zfill(8)

for mask in range(33):
    netw = ip_network(f"{ip}/{mask}", strict=False)
    print(netw)

mask = 26 * "1" + 6 * "0"
m = ''
for i in range(0, 32, 8):
     m += mask[i:i+8]
     m += "."
print(m)

# net = ""
# ipa = ""
# for i in range(0, len(ip), 8):
#     net += n[i:i+8]
#     ipa += ip[i:i+8]
#     net += "."
#     ipa += "."
# print(net)
# print(ipa)