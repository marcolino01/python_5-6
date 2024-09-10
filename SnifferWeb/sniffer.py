from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.http import HTTPRequest 
from scapy.layers.http import HTTPResponse



iPkt = 0

def process_pkt(pkt):
    global iPkt
    print(f"ho ricevuto un pacchetto {iPkt} lungo {pkt[IP].len} sorgente {pkt[IP].src} destinazione {pkt[IP].dst}")

sniff(iface="eth0", filter="tcp", prn=process_pkt)
#nello sniff devo specificare le interfacce di rete per vedere iface vado da terminale con ifconfig
#filter così prendiamo solo i pacchetti tcp
#prn creiamo una procedura e lui chiamerà quella
#pkt è una struttura dati che contiene tutte le info del layer IP pckt[IP]
#pkt[IP].src -> sorgente pkt[IP].dst -> destinazione
#pckt[TCP] abbiamo tutte le info tcp (porte) pkt[TCP].sport -> sorgente pkt[TCP].dport -> destinazione