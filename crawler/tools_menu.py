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
from termcolor import colored, cprint

#Project paths
shuriken_path = os.getcwd()
#Modues paths
wig_path = shuriken_path + "/crawler/WebVuls/wig/wig/wig.py"
#Files single paths
data_single = shuriken_path + "/data/single_data"

tools_text = colored('tool','red')
wig_text = colored('wig_text','red')
crawler_text = colored('crawler', 'red')
nikto_text = colored('nikto', 'red')
geoip_text = colored('geo-ip', 'red')
portScann_text = colored('portScan', 'red')

menu_text = colored('Tools','red')
back_menu_text = colored('Back','blue')
crawler_menu_text = colored('Crawler','blue')
nikto_menu_text = colored('Nikto crawler scan','blue')
nikto_single_menu_text = colored('Nikto single scan','blue')
port_menu_text = colored('Port Scann','blue')
wig_menu_text = colored('Wig','blue')
geo_menu_text = colored('GeoIP','blue')


def back():
	print "[$ "+tools_text+" $] Back main menu \n"

def crawle_start():
	print "[$ "+crawler_text+" $] Start crawler"
	crawlerModule.start_Crawler()

def nikto_start_basic():
	print "[$ "+nikto_text+" $] Start nikto"
	niktoModule.basic_nikto()

def nikto_start_crawler():
	print "[$ "+nikto_text+" $] Start nikto"
	niktoModule.crawler_nikto()

def portScann_start():
	print "[$ "+portScann_text+" $] Start portScann"
	shuriken.main()

def geolocalizeIP_start():
	print "[$ "+geoip_text+" $] Start geoIP"
	localice.main()

def wig_strat():
	print "[$ "+wig_text+" $] Start wig"
	n = raw_input('[$ '+wig_text+' $] Insert url that starts with -www- > ')
	print "[$ "+wig_text+" $] Wig web vulnerability scan is running ...."
	try:
		name = n.split('www')
		folder = name[1].split('.')
		data_wig_path = data_single + "/wig/" +folder[1]
		if not os.path.exists(data_wig_path):
			os.makedirs(data_wig_path)
		f = open(data_wig_path + "/Vuls_wig.txt", "w")
		print "[$ "+wig_text+" $] Creating folder for save results ... " + data_wig_path
		try:
			exit_wig = subprocess.call("python3 " + wig_path + " " + n, shell=True, stdout=f)
			print "[$ "+wig_text+" $] Finish wig scann"
			print "[$ "+wig_text+" $] Output file in " + data_wig_path
		except Exception as e:
			print "[$ "+wig_text+" $] Error : "
			print e
	except Exception as e:
		print "[$ "+wig_text+" $] Error in url format ,try somthing like www.example.com"
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
	
	print "                       - "+menu_text+" -"
	print "                                "
	print "               0 : " + back_menu_text
	print "               1 : " + crawler_menu_text
	print "               2 : " + nikto_menu_text
	print "               3 : " + nikto_single_menu_text
	print "               4 : " + port_menu_text
	print "               5 : " + wig_menu_text
	print "               6 : " + geo_menu_text
	print "\n"
	try:
		inp = raw_input('[$ '+tools_text+' $] Select tool > ')
		n = str(inp)
		if '0' in n or '1' in n or '2' in n or '3' in n or '4' in n or '5' in n or '6' in n or '7' in n:
			options[n]()
		else:
			print('[$ '+tools_text+' $] Is not recognized as a valid command')
			main()
	except KeyboardInterrupt:
		print "Stopping Shuriken"
		sys.exit()