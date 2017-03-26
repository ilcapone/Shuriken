#!/usr/bin/python
# -*- coding: utf-8 -*-

# nikto module

import subprocess
import sys


def basic_nikto():
	webscan = raw_input('[$ nikto $] Insert nikto query to shearch vulneravilitys > ')
	if webscan == None:
		print "[$ nikto $] Error in query!"
		exit()
	print "[$ nikto $] Starting nikto ..."
	switches = webscan
	nikto = "perl WebVuls/nikto/program/nikto.pl " + str(switches)
	subprocess.call(nikto,shell = True)

