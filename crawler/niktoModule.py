#!/usr/bin/python
# -*- coding: utf-8 -*-

# nikto module

import subprocess
import sys
import os
import csv

url_list=['init']


def basic_nikto():
	#f = open("linksVuls_nikto.txt", "w")
	webscan = raw_input('[$ nikto $] Insert nikto query to shearch vulneravilitys > ')
	if webscan == None:
		print "[$ nikto $] Error in query!"
		exit()
	print "[$ nikto $] Starting nikto ..."
	switches = webscan
	nikto = "perl WebVuls/nikto/program/nikto.pl -host " + str(switches) + " -Display -F csv -output data/nikto_basic_scan.csv"
	subprocess.call(nikto,shell = True)
	print "[$ nikto $] Output file linksVuls_nikto.csv"

def crawler_nikto():
	print "[$ nikto $] Start nikto from crawler!"
	print "[$ nikto $] Open data/crawler_links.csv"
	fName= 'data/crawler_links.csv'
	if os.path.exists(fName):
		with open(fName, 'r') as f:
			try:
				reader = csv.reader(f)
				for row in reader:
					print "[$ nikto $] Url"
					check_current_url(row[1])
					print "[$ nikto $] UrlComes"
					check_current_url(row[2])
			except :
				print "[$ nikto $] Error reading data/crawler_links.csv"
	else:
		print "[$ nikto $] The file data/crawler_links.csv don't exist, please first extract de correlated links with scrapy crawler"
	print "[$ nikto $] Output file nikto_crawler_links.csv"

def check_current_url(curr_url):
	checker = False
	for url in url_list:
		if url == curr_url:
			checker = True
	if checker:
		print "[$ nikto $] The url " + curr_url + " has already been scanned"
	else:		
		print "[$ nikto $] The url " + curr_url + " has not been scanned"
		url_list.insert(len(url_list),curr_url)
		launch_nikto(curr_url)

def launch_nikto(url):
	if url == "url":
		print "[$ nikto $] next"
	elif url == "urlComes":
		print "[$ nikto $] next"
	else:
		print "[$ nikto $] Starting nikto scanning " + url
		switches = url
		nikto = "perl WebVuls/nikto/program/nikto.pl -host " + str(switches) + " -Display -F csv -output data/nikto_crawler_links.csv"
		subprocess.call(nikto,shell = True)


