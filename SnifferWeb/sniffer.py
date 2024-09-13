from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.inet import TCP
from scapy.layers.tls.record import TLS
from scapy.layers.http import HTTPRequest 
from scapy.layers.http import HTTPResponse
from datetime import datetime
import csv



"""iPkt = 0

def process_pkt(pkt):
    global iPkt
    print(f"ho ricevuto un pacchetto {iPkt} lungo {pkt[IP].len} sorgente {pkt[IP].src} destinazione {pkt[IP].dst}")

sniff(iface="eth0", filter="tcp", prn=process_pkt)"""
#nello sniff devo specificare le interfacce di rete per vedere iface vado da terminale con ifconfig
#filter così prendiamo solo i pacchetti tcp
#prn creiamo una procedura e lui chiamerà quella
#pkt è una struttura dati che contiene tutte le info del layer IP pckt[IP]
#pkt[IP].src -> sorgente pkt[IP].dst -> destinazione
#pckt[TCP] abbiamo tutte le info tcp (porte) pkt[TCP].sport -> sorgente pkt[TCP].dport -> destinazione


iPkt = 0

def get_tls_sni(pkt):
     try:
        return pkt[TLS].msg[0].ext[0].servernames[0].servername.decode()
     except (IndexError,AttributeError):
          ""


def process_pkt2(pkt):
    global iPkt
    iPkt +=1
    if pkt[IP].sport in [80,443] or pkt[TCP].dport in [80,443]:
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pktIpSrc = pkt[IP].src
        pktIpDst = pkt[IP].dst
        pktTcpSrc = pkt[TCP].sport
        pktTcpDst = pkt[TCP].dport

        host = ""
        if HTTPRequest in pkt:
            if pkt[HTTPRequest].Host:
                host = pkt[HTTPRequest].Host.decode()
        elif TLS in pkt:
            host = get_tls_sni(pkt)
             
        
        if 443 in [pktTcpSrc, pktTcpDst]:
            protocollo = "HTTPS"
        else:
            protocollo = "HTTP"

        with open("file.csv", "a", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow([data, pktIpSrc, pktIpDst, pktTcpSrc, pktTcpDst, host, protocollo])

with open("file.csv", "a", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(["Data","IPSrc","IPDst","TCPSrc","TCPDst","Host","Protocollo"])

    


sniff(iface="eth0", filter="tcp", prn=process_pkt2)




