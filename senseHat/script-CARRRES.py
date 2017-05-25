from scapy.all import *
from sense_hat import SenseHat
from time import sleep

liste_ip = ["8.8.8.8","172.16.0.249","172.16.0.1","192.168.20.251","192.168.12.88","192.168.6.164"]

o = (0,0,0)
b = (64,224,208)
r = (255,0,0)
j = (255,215,0)
v = (0,255,127)

cible = [
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]

sense = SenseHat()
sense.set_rotation(270)

sense.clear()

def testIP (ip):
    req = IP(dst=ip) /ICMP()
    rep = sr1(req, timeout=0.5)
    if not (rep is None):
        print req.dst, "est connecte"
        cible[compteur] = v
    else:
        cible[compteur] = r

compteur = 0
for ip in liste_ip:
    testIP(ip)
    compteur = compteur + 1

sense.set_pixels(cible)
sleep(180)
sense.clear()

