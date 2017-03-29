#!/usr/bin/python
# -*- coding: utf-8 -*-

# shuriken

import subprocess
import sys
import os
import niktoModule
from shurikenCrawler import crawlerModule
from shurikenNmap import shuriken

def info():
	print "\n"
	print "[$ shuriken $] Shuriken is PoC for a final master's work in cybersecurity, for knowlements."
	print "\n"

def exit():
	print "[$ shuriken $] Chao! \n"
	sys.exit()
def crawle_start():
	print "[$ crawler $] Start crawler"
	crawlerModule.start_Crawler()

def nikto_start():
	print "[$ nikto $] Start nikto"
	niktoModule.basic_nikto()

def portScann_start():
	print "[$ portScann $] Start portScann"
	shuriken.main()

def wig_strat():
	f = open("linksVuls_wig.txt", "w")
	print "[$ wig $] Start wig"
	n = raw_input('[$ wig $] Set url > ')
	print "[$ wig $] Wig web vulnerability scan is running ...."
	exit_code = subprocess.call("WebVuls/wig/wig/wig.py " + n, shell=True, stdout=f)
	print "[$ wig $] Output file linksVuls_wig.txt"


options = {'0':exit, '1':info, '2':crawle_start, '3':nikto_start, '4':portScann_start, '5':wig_strat}

def main():
	
	while True:
		print "\n"
		print "             << <$$> Shuriken <$$> >> "
		print "                      "
		print "                    0 : Exit"
		print "                    1 : Info"
		print "                    2 : Crawler"
		print "                    3 : Nikto"
		print "                    4 : Port Scann"
		print "                    5 : Wig"
		print "\n"
		n = raw_input('[$ shuriken $] > ')
		options[n]()

if __name__ == "__main__":
	print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
	print "         _____ _   _ _   _______ _____ _   __ _____ _   _   "
	print " $$$$$  /  ___| | | | | | | ___ \_   _| | / /|  ___| \ | |  $$$$$"
	print "        \ `--.| |_| | | | | |_/ / | | | |/ / | |__ |  \| |  "
	print "  $$$$   `--. \  _  | | | |    /  | | |    \ |  __|| . ` |  $$$$"
	print "        /\__/ / | | | |_| | |\ \ _| |_| |\  \| |___| |\  |  "
	print "    $$  \____/\_| |_/\___/\_| \_|\___/\_| \_/\____/\_| \_/  $$"
	print "                                                           "
	print "      $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
	print " "
	main()