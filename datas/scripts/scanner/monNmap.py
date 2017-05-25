'''
Author : as@u8ik.com

Licence : GPL v3 or any later version

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import nmap
import time
import pickle
import sys
import os

os.system('clear')

try:
    nm = nmap.PortScanner()         # instance of nmap.PortScanner
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(0)

except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(0)

hostList = []
gracePeriod = 7

def seek():    # fonction qui scanne le reseau
    curHosts = [] # On cree une liste vide
    nm.scan(hosts = '172.16.0.0/24', arguments = '-n -sP -PE -T5')
    # 
    # sP execute un ping scan
    # PE
    # T5
    
    localtime = time.asctime(time.localtime(time.time()))

    out = open("outScan.csv", "w")

    #fichier de sortie du scan

    print('============ SCAN ACTUEL {0} ============'.format(localtime))
    # {0} index 0 de format  
    # methode format qui permet de reinjecter les variables facilement

    for host in nm.all_hosts():
        try:
            mac = nm[host]['addresses']['mac']
        except:
            mac = 'unknown'

        curHosts.append((host,mac,gracePeriod))
    
    for host in curHosts:
        Sortie = '%s|%s' % (host[0], host[1])
        print Sortie
        out.write(Sortie+"\n")
    out.close()
    print('Nombre de machines: ' + str(len(curHosts)))
    return len(curHosts) # returne le nombre d'hotes

def EcrireDico():
    """Fonction de traitement.
 
    Lit et traite ligne par ligne le fichier source (src).
    Le resultat est ecrit au fur et a mesure dans le
    fichier destination (dst). 
    """
    monFichier = open("outScan.csv", "r")

    dico = {}
    for ligne in monFichier:
        element = ligne.split("|")
        cle = element[0]
        data = element[1]
        dico[cle] = data
    print "Ecrire du Dico OK"
    #print dico
    monFichier.close()

    f = open( "monScanNmap.p", 'w' )
    P = pickle.Pickler( f )
    P.dump( dico )
    f.close()

def ChercheDif():
    monscan = open('monScanNmap.p','rb')
    MacScan = pickle.load(monscan)    # deserialisation
    monscan.close()

    monparc = open('parcMachines.p','rb')
    MacParc = pickle.load(monparc)    # deserialisation
    monparc.close()

    i = 0
    IPGAUCHE = "172.16.0."
    while i <= 253:
        i = i + 1
        IPGAUCHE = str(IPGAUCHE)
        IPDROITE = i
        IPDROITE = str(IPDROITE)
        #IP = IPGAUCHE+IPDROITE; 
        #print "IP testee "+IP
        IP = str(IPDROITE)
        IPLONGUE = IPGAUCHE + IPDROITE
        try:
            retourMac1 = (MacScan[IPLONGUE])
            #print "################################"
            #print "DEBUG ADRESSE MAC du scan"
            #print retourMac1
            retourMac2 = (MacParc[IPDROITE])
            retourMac2 = str(retourMac2)
            #print "DEBUG ADRESSE MAC du fichier"
            #print retourMac2
            print "################################"
            #print "MAC FICHIER : "+retourMac2
            if retourMac1[0:17] == retourMac2[0:17]:
                print "Adresse Mac de "+IPLONGUE+" OK"
            else:
                if retourMac2 == 'DHCP':
                    print "ADRESSE DYNAMIQUE DHCP"
                    print "IP DHCP : "+IPLONGUE
                else:
                    print "  ______"
                    print " /      \\"
                    print  "| () () |"
                    print  " \  ^  /"
                    print  "  |||||"
                    print  "  |||||"
                    print "XXXXXXXX ARP DIFFERENTE XXXXXXXXXXXXXX"
                    print "IP a verifier : "+IPLONGUE
                    print "Adresse Mac : "+retourMac1[0:17]+" au lieu de "+retourMac2[0:17]
                
        except KeyError:
            #print "IP "+IP+" non trouvee"
            a = "bonjour"
seek()
EcrireDico()
ChercheDif()
