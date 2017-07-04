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
from openvas import openvas_ompController
from termcolor import colored, cprint

#Print collores
shuriken_text = colored('shuriken', 'red')
crawler_text = colored('crawler', 'red')
nikto_text = colored('nikto', 'red')
geoip_text = colored('geo-ip', 'red')
fileResult_text = colored('fileResult','red')
netsecurity_text= colored('net.security','red')
tools_text = colored('tool','red')
controller_text = colored('controller','red')
openvas_text = colored('openvas','red')

#Color Comands
Exit_text = colored('Exit','blue')
info_text = colored('Info','blue')
File_result_text = colored('File result','blue')
Netsecurity_text = colored('Net.security WebApp','blue')
Crawling_proces_text = colored('Crawling proces','blue')
independent_tools_text = colored('Independent tools', 'blue')
OpenVas_text = colored('OpenVas','blue')
kill_text = colored('Kill active processes','blue')

#Menu Colors
Menu_shuriken_text = colored('Shuriken','red')
Menu_proceses_text = colored('Active Processes','red')

# Global parameters for crawler proces storage
crawlerProces_Parameters = dict()

def define_crawlerProces_Parameters(folder, useproxy, proxyIP):
	global crawlerProces_Parameters
	crawlerProces_Parameters['folder'] = folder
	crawlerProces_Parameters['useproxy'] = useproxy
	crawlerProces_Parameters['proxyIP'] = proxyIP
	crawlerModule.define_crawlerProces_Parameters(crawlerProces_Parameters)
	niktoModule.define_crawlerProces_Parameters(crawlerProces_Parameters)
	localice.define_crawlerProces_Parameters(crawlerProces_Parameters)
	nmapCrawler.define_crawlerProces_Parameters(crawlerProces_Parameters)


def info():
	print "\n"
	print "[$ "+shuriken_text+" $] Shuriken is PoC for a final master's work in cybersecurity, for knowlements. Use this tool with caution and do not use it for malicious purposes. The author is not responsible for any damages caused by third parties"
	print "\n"

def exit():
	print "[$ " + shuriken_text +" $] Chao! \n"
	sys.exit()

def crawle_start():
	warning = colored('Start crawler ... ','yellow')
	print "[$ "+crawler_text+" $] " + warning
	crawlerModule.start_Crawler()

def nikto_start_crawler_controller():
	warning = colored('Start nikto from controller ... ','yellow')
	print "[$ "+nikto_text+" $] " + warning
	niktoModule.crawler_nikto_controller()

def geolocalizeIP_start_controller():
	warning = colored('Start geoIP ... ','yellow')
	print "[$ "+geoip_text+" $] " + warning
	localice.crawler_IP()

def file_Result():
	warning = colored('Start file result','yellow')
	print "[$ "+fileResult_text+" $] " + warning
	readData.main()

def net_security():
	warning = colored('Runing Shiny web app ....','yellow')
	print "[$ "+netsecurity_text+" $] " + warning
	ip = raw_input('[$ '+netsecurity_text+' $] Specify the ip where the application will run > ')
	exit_r = subprocess.call("Rscript app.R "+ ip +" &", shell=True)
	print "[$ "+netsecurity_text+" $] Net.Security WebApp"

def independent_tools():
	warning = colored('Start independents tool ..','yellow')
	print "[$ "+tools_text+" $] " +warning
	print "\n"
	tools_menu.main()

def crawler_complet_proces():
	gass()
	folder = raw_input('[$ ' + shuriken_text + ' $] Insert name of the crawler storage > ')
	usenmap = raw_input('[$ ' + shuriken_text + ' $] You want to use nmap? (y/n) > ')
	useproxy = raw_input('[$ ' + shuriken_text + ' $] You want to use proxy? (y/n) > ')
	if 'y' in useproxy:
		proxyIP = raw_input('[$ ' + shuriken_text + ' $] Insert proxy ip and port (IP:PORT) > ')
	else:
		proxyIP=None
	define_crawlerProces_Parameters(folder, useproxy, proxyIP)
	warning = colored('Start complet crawler process ..','yellow')
	print "[$ "+controller_text+" $] " + warning
	crawle_start()
	warning = colored('Start nikto crawler process ..','yellow')
	print "[$ "+controller_text+" $] " + warning
	nikto_start_crawler_controller()
	if 'y' in usenmap and len(usenmap)==1:
		warning = colored('Start nmap process ..','yellow')
		print "[$ "+controller_text+" $] " + warning
		nmapCrawler.crawler_nmap_controller()
	warning = colored('Start complet geo Ip process ..','yellow')
	print "[$ "+controller_text+" $] " + warning
	geolocalizeIP_start_controller()
	warning = colored('End crawler process','yellow')
	print "[$ "+controller_text+" $] " + warning

def start_openvas():
	warning = colored('Start Openvas tool ..','yellow')
	print "[$ "+openvas_text+" $] " + warning
	print "\n"
	openvas_ompController.main()

def kill_process():
	warning = colored('Be careful you could stop some important process !!','yellow')
	print "[$ "+shuriken_text+" $] " + warning
	pid_proces = raw_input('[$ ' + shuriken_text + ' $] Insert the process PID > ')
	subprocess.call('kill -9 ' + pid_proces ,shell = True)
	print "[$ "+shuriken_text+" $] The process " + pid_proces + " has been stopped"
	print "\n"


options = {
'0':exit,
'1':info,
'2':file_Result,
'3':net_security,
'4':crawler_complet_proces,
'5':independent_tools,
'6':start_openvas,
'7':kill_process}

def main():

	while True:

		results_openvas = subprocess.check_output("ps aux | grep openvasmd", shell=True)
		results_openvas = results_openvas.split('\n')
		for result in results_openvas:
			if 'grep' in result or '' in result and len(result)==0:
				pass
			else:
				result = result.split(' ')
				try:
					results_openvas = str("PID > " + result[6] + "   Process > " + result[28])
				except:
					try:
						results_appR = str("PID > " + result[6] + "   Process > " + result[27
							])
					except Exception, e:
						print result
						print e

		results_appR = subprocess.check_output("ps aux | grep app.R", shell=True)
		results_appR = results_appR.split('\n')
		for result in results_appR:
			if 'grep' in result or '' in result and len(result)==0:
				pass
			else:
				result = result.split(' ')
				try:
					results_appR = str("PID > " + result[6] + "   Process > " + result[25] + "" + result[28] + "" + result[29] +" " + result[30])
				except:
					try:
						results_appR = str("PID > " + result[6] + "   Process > " + result[24] + "" + result[27] + "" + result[28] +" " + result[29])
					except:
						try:
							results_appR = str("PID > " + result[6] + "   Process > " + result[23] + "" + result[26] + "" + result[27] +" " + result[28])
						except Exception, e:
							print result
							print e
		
		if type(results_openvas) == list:
			results_openvas = ''
		if type(results_appR) == list:
			results_appR = ''

		print "\n"
		print "        << <$$> "+Menu_shuriken_text+" <$$> >>                         -- -- "+Menu_proceses_text+" -- --"
		print "                                             |"
		print "              0 : "+Exit_text+"                       |"
		print "              1 : "+info_text+"                       |         " + results_openvas
		print "              2 : "+File_result_text+"                |"
		print "              3 : "+Netsecurity_text+"        |         " + results_appR
		print "              4 : "+Crawling_proces_text+"            |"
		print "              5 : "+independent_tools_text+"          |"
		print "              6 : "+OpenVas_text+"                    |"
		print "              7 : "+kill_text+"      |"
		print "\n"
		try:
			inp = raw_input('[$ ' + shuriken_text + ' $] > ')
			n = str(inp)
			if '0' in n or '1' in n or '2' in n or '3' in n or '4' in n or '5' in n or '6' in n or '7' in n:
				options[n]()
			else:
				print('[$ ' + shuriken_text + ' $] Is not recognized as a valid command')
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
	title_text1 = colored('   ▄████████    ▄█    █▄    ███    █▄     ▄████████  ▄█     ▄█   ▄█▄    ▄████████ ███▄▄▄▄   ','red')
	title_text2 = colored('  ███    ███   ███    ███   ███    ███   ███    ███ ███    ███ ▄███▀   ███    ███ ███▀▀▀██▄ ','red')
	title_text3 = colored('  ███    █▀    ███    ███   ███    ███   ███    ███ ███▌   ███▐██▀     ███    █▀  ███   ███ ','red')
	title_text4 = colored('  ███         ▄███▄▄▄▄███▄▄ ███    ███  ▄███▄▄▄▄██▀ ███▌  ▄█████▀     ▄███▄▄▄     ███   ███ ','red')
	title_text5 = colored('▀███████████ ▀▀███▀▀▀▀███▀  ███    ███ ▀▀███▀▀▀▀▀   ███▌ ▀▀█████▄    ▀▀███▀▀▀     ███   ███ ','red')
	title_text6 = colored('         ███   ███    ███   ███    ███ ▀███████████ ███    ███▐██▄     ███    █▄  ███   ███ ','red')
	title_text7 = colored('   ▄█    ███   ███    ███   ███    ███   ███    ███ ███    ███ ▀███▄   ███    ███ ███   ███ ','red')
	title_text8 = colored(' ▄████████▀    ███    █▀    ████████▀    ███    ███ █▀     ███   ▀█▀   ██████████  ▀█   █▀  ','red')

	doct_text = colored('.','red')
	star_text = colored('*','red')
	dolar_text = colored('$','red')

	
	print ""
	print ""+title_text1
	print ""+title_text2
	print ""+title_text3
	print ""+title_text4
	print ""+title_text5
	print ""+title_text6
	print ""+title_text7
	print ""+title_text8
	print "  "
	print "  "
	#print "          $"+dolar_text+"$"+dolar_text+"$  $"+dolar_text+"$"+dolar_text+"$  $"+dolar_text+"$"+dolar_text+"$  $"+dolar_text+"$"+dolar_text+"$  $"+dolar_text+"$"+dolar_text+"$  $"+dolar_text+"$"+dolar_text+"$  $"+dolar_text+"$"+dolar_text+"$  $"+dolar_text+"$"+dolar_text+"$"
	#print "           $"+dolar_text+"$    $"+dolar_text+"$    $"+dolar_text+"$    $"+dolar_text+"$    $"+dolar_text+"$    $"+dolar_text+"$    $"+dolar_text+"$    $"+dolar_text+"$"
	print "            $      $      $      $      $      $      $      $"
	print "            "+star_text+"      "+star_text+"      "+star_text+"      "+star_text+"      "+star_text+"      "+star_text+"      "+star_text+"      "+star_text
	print "            *      *      *      *      *      *      *      *"
	print "            "+star_text+"      "+star_text+"      "+star_text+"      "+star_text+"      "+star_text+"      "+star_text+"      "+star_text+"      "+star_text
	print "            "+star_text+"      "+star_text+"      "+star_text+"      "+star_text+"      "+star_text+"      "+star_text+"      "+star_text+"      "+star_text
	print "            "+doct_text+"      "+doct_text+"      "+doct_text+"      "+doct_text+"      "+doct_text+"      "+doct_text+"      "+doct_text+"      "+doct_text
	main()