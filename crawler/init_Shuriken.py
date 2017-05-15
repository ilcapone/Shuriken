#!/usr/bin/python
# -*- coding: utf-8 -*-

# shuriken

import subprocess
import sys
import os
import niktoModule
from shurikenCrawler import crawlerModule
from shurikenNmap import shuriken
from shurikenGeoIP import localice
from shurikenReadData import readData

def info():
	print "\n"
	print "[$ shuriken $] Shuriken is PoC for a final master's work in cybersecurity, for knowlements. Use this tool with caution and do not use it for malicious purposes. The author is not responsible for any damages caused by third parties"
	print "\n"

def exit():
	print "[$ shuriken $] Chao! \n"
	sys.exit()
def crawle_start():
	print "[$ crawler $] Start crawler"
	crawlerModule.start_Crawler()

def nikto_start_basic():
	print "[$ nikto $] Start nikto"
	niktoModule.basic_nikto()

def nikto_start_crawler():
	print "[$ nikto $] Start nikto"
	niktoModule.crawler_nikto()

def portScann_start():
	print "[$ portScann $] Start portScann"
	shuriken.main()

def geolocalizeIP_start():
	print "[$ geo-ip $] Start geoIP"
	localice.main()

def wig_strat():
	f = open("data/Vuls_wig.txt", "w")
	print "[$ wig $] Start wig"
	n = raw_input('[$ wig $] Set url > ')
	print "[$ wig $] Wig web vulnerability scan is running ...."
	exit_code = subprocess.call("python3 WebVuls/wig/wig/wig.py " + n, shell=True, stdout=f)
	print "[$ wig $] Output file in data/Vuls_wig.txt"

def file_Result():
	print "[$ fileResult $] Start file result"
	readData.main()



options = {'0':exit, '1':info, '2':crawle_start, '3':nikto_start_crawler, '4':nikto_start_basic, '5':portScann_start, '6':wig_strat, '7':geolocalizeIP_start, '8':file_Result}

def main():
	
	while True:
		print "\n"
		print "                        << <$$> Shuriken <$$> >> "
		print "                                 "
		print "                               0 : Exit"
		print "                               1 : Info"
		print "                               2 : Crawler"
		print "                               3 : Nikto crawler scan"
		print "                               4 : Nikto single scan"
		print "                               5 : Port Scann"
		print "                               6 : Wig"
		print "                               7 : GeoIP"
		print "                               8 : File result"

		print "\n"
		try:
			n = raw_input('[$ shuriken $] > ')
			options[n]()
		except KeyboardInterrupt:
			print "Stopping Shuriken"
			sys.exit()
		

if __name__ == "__main__":
	print "==========================================================================="
	print ""
	print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
	print " $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
	print "  $$$$$$$$   _____ _   _ _   _______ _____ _   __ _____ _   _   $$$$$$$$"
	print "   $$$$$$$  /  ___| | | | | | | ___ \_   _| | / /|  ___| \ | |  $$$$$$$"
	print "    $$$$$$  \ `--.| |_| | | | | |_/ / | | | |/ / | |__ |  \| |  $$$$$$"
	print "     $$$$$   `--. \  _  | | | |    /  | | |    \ |  __|| . ` |  $$$$$"
	print "      $$$$  /\__/ / | | | |_| | |\ \ _| |_| |\  \| |___| |\  |  $$$$"
	print "       $$$  \____/\_| |_/\___/\_| \_|\___/\_| \_/\____/\_| \_/  $$$"
	print "        $$                                                      $$"
	print "         $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
	print "          $$$$$  $$$$$  $$$$$  $$$$$  $$$$$  $$$$$  $$$$$  $$$$$"
	print "           $$$    $$$    $$$    $$$    $$$    $$$    $$$    $$$"
	print "            $      $      $      $      $      $      $      $"
	print "            *      *      *      *      *      *      *      *"
	print "            *      *      *      *      *      *      *      *"
	print "            *      *      *      *      *      *      *      *"
	print "            *      *      *      *      *      *      *      *"
	print "            .      .      .      .      .      .      .      ."
	main()