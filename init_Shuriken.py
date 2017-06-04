#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# shuriken

import subprocess
import sys
import os
from crawler import niktoModule
from crawler import tools_menu
from crawler.shurikenCrawler import crawlerModule
from crawler.shurikenNmap import shuriken
from crawler.shurikenNmap import nmapCrawler
from crawler.shurikenGeoIP import localice
from crawler.shurikenReadData import readData

#Project paths
#shuriken_path = os.getcwd()
#Modues paths
#wig_path = shuriken_path + "/crawler/WebVuls/wig/wig/wig.py"
#Files paths
#data = shuriken_path + "/crawler/data"
#Files crawler paths
#data_crawler = shuriken_path + "/data/crawler_data"
#Files single paths
#data_single = shuriken_path + "/data/single_data"

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

def nikto_start_crawler_controller():
	print "[$ nikto $] Start nikto from controller"
	niktoModule.crawler_nikto_controller()

def geolocalizeIP_start():
	print "[$ geo-ip $] Start geoIP"
	localice.main()

def file_Result():
	print "[$ fileResult $] Start file result"
	readData.main()

def net_security():
	print "[$ net.security $]  Runing Shiny web app ...."
	exit_r = subprocess.call("Rscript app.R &", shell=True)
	print "[$ net.security $] Net.Security WebApp"

def independent_tools():
	print "\n"
	tools_menu.main()

def crawler_complet_proces():
	gass()
	print "[$ controller $] Start complet crawler process .."
	crawle_start()
	print "[$ controller $] Start complet nikto process .."
	nikto_start_crawler_controller()
	print "[$ controller $] Start complet nmap process .."
	nmapCrawler.crawler_nmap_controller()
	print "[$ controller $] Start complet geo Ip process .."
	geolocalizeIP_start()
	print "[$ controller $] End crawler process"


options = {
'0':exit,
'1':info,
'2':file_Result,
'3':net_security,
'4':crawler_complet_proces,
'5':independent_tools}

def main():
	
	while True:
		print "\n"
		print "                        << <$$> Shuriken <$$> >> "
		print "                                 "
		print "                               0 : Exit"
		print "                               1 : Info"
		print "                               2 : File result"
		print "                               3 : Net.security WebApp"
		print "                               4 : Crawling proces"
		print "                               5 : Independent tools"
		print "\n"
		try:
			inp = raw_input('[$ shuriken $] > ')
			n = str(inp)
			if '0' in n or '1' in n or '2' in n or '3' in n or '4' in n or '5' in n:
				options[n]()
			else:
				print('[$ shuriken $] Is not recognized as a valid command')
				main()
		except KeyboardInterrupt:
			print "Stopping Shuriken"
			sys.exit()
def gass():
	print "\n"
	print '  /$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$$'
	print ' /$$__  $$ |____  $$ /$$_____//$$_____/'
	print '| $$  \ $$  /$$$$$$$|  $$$$$$|  $$$$$$ '
	print '| $$  | $$ /$$__  $$ \____  $$\____  $$'
	print '|  $$$$$$$|  $$$$$$$ /$$$$$$$//$$$$$$$/'
	print ' \____  $$ \_______/|_______/|_______/ '
	print ' /$$  \ $$                             '
	print '|  $$$$$$/                             '
	print  '\______/                              '
	print "\n"

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