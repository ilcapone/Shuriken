#!/usr/bin/python
# -*- coding: utf-8 -*-

# nikto module

import subprocess
import sys
import os
import csv

url_list=['init']

def __init__():
	proxy=None

def basic_nikto():
	webscan = raw_input('[$ nikto $] Insert nikto query to shearch vulneravilitys > ')
	if webscan == None:
		print "[$ nikto $] Error in query!"
		exit()
	switches = webscan
	px = raw_input('[$ nikto $] You want to use proxy? (y/n) > ')
	if px == 'y':
		ip_port = raw_input('[$ nikto $] Insert proxy IP:PORT > ')
		proxy = '-useproxy http://'+ str(ip_port) +'/'
		print "[$ nikto $] Starting nikto ... adicional param: " + str(proxy)
		nikto = "perl WebVuls/nikto/program/nikto.pl -host " + str(switches) + " " + str(proxy) +" -Display -F csv -output data/nikto_basic_scan.csv"
		print(nikto)
		subprocess.call(nikto,shell = True)
	else:
		print "[$ nikto $] Starting nikto ..."
		nikto = "perl WebVuls/nikto/program/nikto.pl -host " + str(switches) + " -Display -F csv -output data/nikto_basic_scan.csv"
		subprocess.call(nikto,shell = True)

	print "[$ nikto $] Output file data/nikto_basic_scan.csv"

def crawler_nikto():
	print "[$ nikto $] Start nikto from crawler!"
	print "[$ nikto $] Open data/crawler_links.csv"
	px = raw_input('[$ nikto $] You want to use proxy? (y/n) > ')
	if px == 'y':
		ip_port = raw_input('[$ nikto $] Insert proxy IP:PORT > ')
		proxy = '-useproxy http://'+ str(ip_port) +'/'
	else:
		proxy = None
	fName= 'data/crawler_links.csv'
	if os.path.exists(fName):
		with open(fName, 'r') as f:
			try:
				reader = csv.reader(f)
				for row in reader:
					print "[$ nikto $] Url"
					check_current_url(row[1], proxy)
					print "[$ nikto $] UrlComes"
					check_current_url(row[2], proxy)
			except :
				print "[$ nikto $] Error reading data/crawler_links.csv"
	else:
		print "[$ nikto $] The file data/crawler_links.csv don't exist, please first extract de correlated links with scrapy crawler"
	print "[$ nikto $] Output file nikto_crawler_links.csv"

def check_current_url(curr_url, proxy):
	checker = False
	for url in url_list:
		if url == curr_url:
			checker = True
	if checker:
		print "[$ nikto $] The url " + curr_url + " has already been scanned"
	else:		
		print "[$ nikto $] The url " + curr_url + " has not been scanned"
		url_list.insert(len(url_list),curr_url)
		launch_nikto(curr_url, proxy)

def launch_nikto(url, proxy):
	if url == "url":
		print "[$ nikto $] next"
	elif url == "urlComes":
		print "[$ nikto $] next"
	else:
		print "[$ nikto $] Starting nikto scanning " + url
		switches = url
		if proxy is not None:
			print "[$ nikto $] Starting nikto ... adicional param: " + str(proxy)
			nikto = "perl WebVuls/nikto/program/nikto.pl -host " + str(switches) + " " + str(proxy) +" -Display -F csv -output data/nikto_crawler_links.csv"
			subprocess.call(nikto,shell = True)
		else:
			print "[$ nikto $] Starting nikto ..."
			nikto = "perl WebVuls/nikto/program/nikto.pl -host " + str(switches) + " -Display -F csv -output data/nikto_crawler_links.csv"
			subprocess.call(nikto,shell = True)