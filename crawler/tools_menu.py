#!/usr/bin/python
# -*- coding: utf-8 -*-

# independent tools

import sys
import os
import subprocess
from crawler import niktoModule
from crawler.shurikenCrawler import crawlerModule
from crawler.shurikenNmap import shuriken
from crawler.shurikenNmap import nmapCrawler
from crawler.shurikenGeoIP import localice
from crawler.shurikenReadData import readData

#Project paths
shuriken_path = os.getcwd()
#Modues paths
wig_path = shuriken_path + "/crawler/WebVuls/wig/wig/wig.py"
#Files single paths
data_single = shuriken_path + "/data/single_data"

def back():
	print "[$ tools $] Back main menu \n"

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
	print "[$ wig $] Start wig"
	n = raw_input('[$ wig $] Insert url that starts with -www- > ')
	print "[$ wig $] Wig web vulnerability scan is running ...."
	try:
		name = n.split('www')
		folder = name[1].split('.')
		data_wig_path = data_single + "/wig/" +folder[1]
		if not os.path.exists(data_wig_path):
			os.makedirs(data_wig_path)
		f = open(data_wig_path + "/Vuls_wig.txt", "w")
		print "[$ wig $] Creating folder for save results ... " + data_wig_path
		try:
			exit_wig = subprocess.call("python3 " + wig_path + " " + n, shell=True, stdout=f)
			print "[$ wig $] Finish wig scann"
			print "[$ wig $] Output file in " + data_wig_path
		except Exception as e:
			print "[$ wig $] Error : "
			print e
	except Exception as e:
		print "[$ wig $] Error in url format ,try somthing like www.example.com"
		print e

options = {
'0':back,
'1':crawle_start,
'2':nikto_start_crawler,
'3':nikto_start_basic,
'4':portScann_start,
'5':wig_strat,
'6':geolocalizeIP_start
}

def main():
	print "                       - Tools -"
	print "                                "
	print "               0 : Back"
	print "               1 : Crawler"
	print "               2 : Nikto crawler scan"
	print "               3 : Nikto single scan"
	print "               4 : Port Scann"
	print "               5 : Wig"
	print "               6 : GeoIP"
	print "\n"
	try:
		inp = raw_input('[$ tools $] Select tool > ')
		n = str(inp)
		if '0' in n or '1' in n or '2' in n or '3' in n or '4' in n or '5' in n or '6' in n or '7' in n:
			options[n]()
		else:
			print('[$ tools $] Is not recognized as a valid command')
			main()
	except KeyboardInterrupt:
		print "Stopping Shuriken"