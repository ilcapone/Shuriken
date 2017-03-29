#!/usr/bin/python
# -*- coding: utf-8 -*-

# nikto module

import subprocess
import sys


def basic_nikto():
	#f = open("linksVuls_nikto.txt", "w")
	webscan = raw_input('[$ nikto $] Insert nikto query to shearch vulneravilitys > ')
	if webscan == None:
		print "[$ nikto $] Error in query!"
		exit()
	print "[$ nikto $] Starting nikto ..."
	switches = webscan
	nikto = "perl WebVuls/nikto/program/nikto.pl -host " + str(switches) + " -Display V -F csv -output data/links_Vulsnikto.csv"
	subprocess.call(nikto,shell = True)
	print "[$ nikto $] Output file linksVuls_nikto.csv"

