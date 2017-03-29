#!/usr/bin/python
# -*- coding: utf-8 -*-

# scapy

import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

def Stealth():
	src_port = RandShort()
	dst_ip = raw_input('[$ scapy $] Insert Host > ')
	dest_ports = raw_input('[$ scapy $] Insert Ports > ')
	dest_ports.replace(" ","")
	scanPorts = dest_ports.strip().split(':')

	for port in scanPorts:
		response = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=int(port),flags="S"))

		if (str(type(response))=="<type 'NoneType'>"):
			print port+": Filtered"

		elif (response.haslayer(TCP)):
			if (response.getlayer(TCP).flags == 0x12):
				send_rst=srl(IP(dst=dst_ip)/TCP(sport=src_port,dport=int(port),flags='R'))
				print port+": Open"

		elif (response.getlayer(TCP).flags == 0x14):
			print port+": Closed"
		elif (response.getlayer(ICMP)):
			if(int(response.getlayer(ICMP).type)==3 and int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]):
				print port+": Filtered (ICMP result)"

def udpScan():
	src_port = RandShort()
	dst_ip = raw_input('[$ scapy $] Insert Host > ')
	dest_ports = raw_input('[$ scapy $] Insert Ports > ')
	dest_ports.replace(" ","")
	scanPorts = dest_ports.strip().split(':')

	for port in scanPorts:
		response = sr1(IP(dst=dst_ip)/UDP(dport=int(port)))

		if (str(type(response))=="<type 'NoneType'>"):
			retrans=[]
			for count in range (0,3):
				retrans.append(sr1(IP(dst=dst_ip)/UDP(dport=int(port))))
				for item in retrans:
					if (response.haslayer(UDP)):
						print port+": Open"
					elif (response.haslayer(ICMP)):
						if (int(response.getlayer(ICMP).type)== 3 and int(response.getlayer(ICMP).code)==3 ):
							print port + ": Closed"
					elif (int(response.getlayer(ICMP).type)==3 and int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]):
						print port + ": Filtered"

def basic_scan():
	dst_ip = raw_input('[$ scapy $] Insert Host > ')
	min_port = raw_input('[$ scapy $] Enter minimun port number > ')
	max_port = raw_input('[$ scapy $] Enter maximun port number > ')
	loop_break = 0
	try:
		if int(min_port) >= 0 and int(max_port >=0) and int(max_port) >= int(min_port):
			pass
		else:
			print "\n [$ scapy $] Invalid range of ports"
	except Exception:
		print "\n [$ scapy $] Invalid range of ports"

	ports = range(int(min_port), int(max_port))
	SYNACK = 0x12
	RSTACK = 0x14

	try:
		ping = sr1 (IP(dst = dst_ip)/ICMP())
		print "\n[$ scapy $] Host is Up, Beginning scan ..."
	except Exception:
		print "\n[$ scapy $] Couldn't resolve host"
	for port in ports:
		print "\n[$ scapy $ Send packet {}".format(loop_break)
		status = scanport(port,dst_ip)
		if status == True:
			print "Port " + str(port)+ ": Open"
		loop_break= loop_break +1
		if loop_break == 5:
			break



def scanport(port,dst_ip):
	srcport = RandShort()
	conf.verb = 0
	SYNACKpkt = sr1(IP(dst=dst_ip)/TCP(sport=srcport,dport=port,flags="S"))
	pktflags = SYNACKpkt.getlayer(TCP).flags
	if pktflags == SYNACK:
		return True
	else:
		return False
	RSTpkt = IP(dst = dst_ip)/TCP(sport = srcport, dport=port, flags ="R")
	send(RSTpkt)

def back():
	print "[$ scapy $] Back portScann menu \n"


options = {'0': Stealth, '1': udpScan, '2':basic_scan, '3':back}

def scapyMenu():
	print "                       - Scapy Options -"
	print "               0 : Stealth scan"
	print "               1 : UDP scan  "
	print "               2 : Basic scan  "
	print "               3 : Back "
	n = raw_input('[$ scapy $]] > ')
	options[n]()
