#!/usr/bin/python
# -*- coding: utf-8 -*-

# nmap

import sys
import nmap

class NmapHost:
	def __init__(self):
		self.host = None
		self.state = None
		self.state = None
		self.openPorts = []
		self.closedFilteredPorts = []

class NmaoPort:
	def __init__(self):
		self.id = None
		self.state = None
		self.reason = None
		self.port = None
		self.name = None
		self.version = None
		self.scriptOutput = None

def parseNmapScan(scan):
	nmapHosts = []
	for host in scan.all_hosts():
		nmapHost = NmapHost()
		nmapHost.host = host
		if scan[host].has_key('status'):
			nmapHost.state = scan[host]['status']['state']
			nmapHost.reason = scan[host]['status']['reason']
			for protocol in ["tcp","udp","icmp"]:
				if scan[host].has_key(protocol):
					ports = scan[host][protocol].keys()
					for port in ports:
						nmapPort = NmaoPort()
						nmapPort.port = port
						nmapPort.state = scan[host][protocol][port]['state']
						if scan[host][protocol][port].has_key('script'):
							nmapPort.scriptOutput = scan[host][protocol][port]['script']
						if scan[host][protocol][port].has_key('reason'):
							nmapPort.reason = scan[host][protocol][port]['reason']
						if scan[host][protocol][port].has_key('name'):
							nmapPort.name = scan[host][protocol][port]['name']
						if scan[host][protocol][port].has_key('version'):
							nmapPort.version = scan[host][protocol][port]['version']
						if 'open' in (scan[host][protocol][port]['state']):
							nmapHost.openPorts.append(nmapPort)
						else:
							nmapHost.closedFilteredPorts.append(nmapPort)
					nmapHosts.append(nmapHost)
					print " Host add to structure!"
		else:
			print "[$ nmap $] There is no match in the Nmap scan with the specified protocol %s" (protocol)
			return nmapHost

def basic_scan():
	nm = nmap.PortScanner()
	ip = raw_input('[$ nmap $] Insert Host > ')
	portRank = raw_input('[$ nmap $] Insert Port rank (portinit-finalport) > ')
	nm.scan(ip, portRank)
	print nm.csv()
	for h in nm.all_hosts():
		if 'mac' in nm[h]['addresses']:
			print(nm[h]['addresses'], nm[h]['vendor'])
	structureNmap = parseNmapScan(nm)
	print "\n"

def arguments_scan():
	nm = nmap.PortScanner()
	ip = raw_input('[$ nmap $] Insert Host > ')
	portRank = raw_input('[$ nmap $] Insert Port rank (portinit-finalport) > ')
	argument = raw_input('[$ nmap $] Insert Arguments > ')
	nm.scan(ip, arguments=argument)
	print nm.csv()
	print('[$ nmap $] Host : %s (%s)' % (ip, nm[ip].hostname()))
	print('[$ nmap $] State : %s' % nm[ip].state())
	for host in nm.all_hosts():
		if 'mac' in nm[host]['addresses']:
			print(nm[host]['addresses'], nm[host]['vendor'])
	structureNmap = parseNmapScan(nm)
	print "\n"

def evade_ids():
	nm = nmap.PortScanner()
	ip = raw_input('[$ nmap $] Insert Host > ')
	portRank = raw_input('[$ nmap $] Insert Port rank (portinit-finalport) > ')
	print "[$ nmap $] --spoof-mac Cisco -T4 --source-port 53 -sS --send-ip -n --data-length 30 --randomize-hosts -n -f -f -sV --version-all -O"
	nm.scan(ip, arguments='--spoof-mac Cisco -T4 --source-port 53 -sS --send-ip -n --data-length 30 --randomize-hosts -n -f -f -sV --version-all -O')
	print nm.csv()
	for host in nm.all_hosts():
		if 'mac' in nm[host]['addresses']:
			print(nm[host]['addresses'], nm[host]['vendor'])
	structureNmap = parseNmapScan(nm)
	print "\n"

def back():
	print "[$ nmap $] Back portScann menu \n"


options = {'0': basic_scan, '1': arguments_scan, '2': evade_ids, '3': back}

def nmapMenu():
	print "                       - Nmap Options -"
	print "               0 : Basic scan"
	print "               1 : Scan with arguments"
	print "               2 : Scan evade IDS"
	print "               3 : Back"
	n = raw_input('[$ nmap $] > ')
	options[n]()