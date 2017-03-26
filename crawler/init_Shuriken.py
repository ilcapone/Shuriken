#!/usr/bin/python
# -*- coding: utf-8 -*-

# shuriken

import sys
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
	print "[$ crawler $] Start crawler \n"
	crawlerModule.start_Crawler()

def nikto_start():
	print "[$ nikto $] Start nikto \n"
	niktoModule.basic_nikto()

def portScann_start():
	print "[$ portScann $] Start portScann"
	shuriken.main()


options = {'0':info, '1':exit, '2':crawle_start, '3':nikto_start, '4':portScann_start}

def main():
	
	while True:
		print "                     << <$$> Shuriken <$$> >> "
		print "                       - Main menu Options -"
		print "               0 : Info"
		print "               1 : Exit"
		print "               2 : Crawler"
		print "               3 : Nikto"
		print "               4 : Port Scann"
		n = raw_input('[$ shuriken $] > ')
		options[n]()

if __name__ == "__main__":
	print " _____ _   _ _   _______ _____ _   __ _____ _   _ "
	print "/  ___| | | | | | | ___ \_   _| | / /|  ___| \ | |"
	print "\ `--.| |_| | | | | |_/ / | | | |/ / | |__ |  \| |"
	print " `--. \  _  | | | |    /  | | |    \ |  __|| . ` |"
	print "/\__/ / | | | |_| | |\ \ _| |_| |\  \| |___| |\  |"
	print "\____/\_| |_/\___/\_| \_|\___/\_| \_/\____/\_| \_/\n"
	main()