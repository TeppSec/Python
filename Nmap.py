#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("<-- Nmap port scanner -->")
print("<----------------------------------------------------->")
ip_addr = input("Enter IP-Addr: ")
type(ip_addr)