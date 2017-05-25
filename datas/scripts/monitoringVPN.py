#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

from scapy.all import *
import time
import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

os.system('clear')

#liste des routeurs distants : 
#192.168.12.88,192.168.6.252, 192.168.2.252, 192.168.4.252
#10.10.10.252

liste_ip = ["192.168.12.88", "192.168.6.164","192.168.20.217"]

def envoiMail (ip):
   msg = MIMEMultipart()
   msg['From'] = 'admin@mtemtf.com'
   msg['To'] = 'salcaraz@mtemtf.com'
   msg['Subject'] = str(ip)+' Hors ligne !' 
   message = str(ip)+' Hors ligne !'
   msg.attach(MIMEText(message))
   mailserver = smtplib.SMTP('ns0.ovh.net', 587)
   mailserver.ehlo()
   mailserver.login('chabe@mtemtf.com', 'che47u')
   mailserver.sendmail('salcaraz@mtemtf.com', 'salcaraz@mtemtf.com', msg.as_string())
   mailserver.quit()

def testIp (ip):

   req = IP(dst=ip) /ICMP()
   rep = sr1(req, timeout=0.5)

   if not (rep is None):
      print req.dst, "est connecte"
   else:
      envoiMail(ip)

      #print req.dst, "est deconnecte"
      #time.sleep(4)
      
for ip in liste_ip:
   testIp(ip)
