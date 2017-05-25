from scapy.all import *

rang = '172.16.0.1-10'

rep, non_rep = sr( IP(dst=rang) / ICMP(), timeout=0.5)

for elem in rep:
    if elem[1].type == 0:
        print elem[1].src + ' a envoye un echo-reply '
