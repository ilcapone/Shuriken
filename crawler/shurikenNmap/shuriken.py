#!/usr/bin/python
# -*- coding: utf-8 -*-

# shuriken

import sys
import nmapScan
import scapyScan
import nmapCrawler

def back():
	print "[$ portScann $] Back main menu \n"

options = {'0':nmapScan.nmapMenu,'1':scapyScan.scapyMenu, '2':nmapCrawler.crawler_nmap, '3':back}

def main():
	print "                       - portScan Oprions -"
	print "               0 : Nmap scan"
	print "               1 : Scapy scan"
	print "               2 : Crawler nmap scan"
	print "               3 : Back"
	n = raw_input('[$ portScann $] > ')
	options[n]()