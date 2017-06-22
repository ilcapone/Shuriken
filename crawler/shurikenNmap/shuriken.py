#!/usr/bin/python
# -*- coding: utf-8 -*-

# shuriken

import sys
import nmapScan
import scapyScan
import nmapCrawler

def back():
	print "[$ portScann $] Back main menu \n"

options = {'0': back,'1':scapyScan.scapyMenu, '2':nmapCrawler.crawler_nmap, '3':nmapScan.nmapMenu}

def main():
	print "\n"
	print "                       - portScan Options -"
	print ""
	print "               0 : Back"
	print "               1 : Scapy scan"
	print "               2 : Crawler nmap scan"
	print "               3 : Nmap scan"
	print "\n"
	n = raw_input('[$ portScann $] > ')
	options[n]()