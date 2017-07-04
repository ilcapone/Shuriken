#!/usr/bin/python
# -*- coding: utf-8 -*-

# read file resut

import sys
import os
import subprocess
from termcolor import colored, cprint

proyect_path = os.getcwd()
data = proyect_path + "/data"
crawler_path = proyect_path + "/data/crawler_data"
netSecurity_path = proyect_path + "/data/netSecurity_data"
openvas_path = proyect_path + "/data/openvas"

menu_text = colored('fileResult Options','red')
fileResult_text = colored('fileResult','red')
files_folders_text = colored('View files in folder','blue')
back_text = colored('Back','blue')
result_text = colored('View result content','blue')
update_text = colored('Update netSecurity results','blue')


def back():
	print "[$ "+fileResult_text+" $] Back main menu \n"

def viewFiles():
	print "[$ "+fileResult_text+" $] Current result directory: " + crawler_path
	files = os.listdir(crawler_path)
	print "[$ "+fileResult_text+" $] Crawler files: "
	for file in files:
		if '__init__.py' in file or '__init__.pyc' in file or 'readData.py' in file or 'readData.pyc' in file:
			i=0
		else:
			if '.csv' in file:
				print file
			else:
				files_subfolder = os.listdir(crawler_path + "/" + file)
				subfoler = colored('Subfoler > ' + file,'yellow')
				print(subfoler)
				for fl in files_subfolder:
					print "--- " + fl

	print "\n"
	print "[$ "+fileResult_text+" $] Current result directory: " + netSecurity_path
	files = os.listdir(netSecurity_path)
	print "[$ "+fileResult_text+" $] Net Security files: "
	for file in files:
		if '__init__.py' in file or '__init__.pyc' in file or 'readData.py' in file or 'readData.pyc' in file:
			i=0
		else:
			if '.csv' in file:
				print file
			else:
				files_subfolder = os.listdir(netSecurity_path + "/" + file)
				subfoler = colored('Subfoler > ' + file,'yellow')
				print(subfoler)
				for fl in files_subfolder:
					print "--- " + fl
	print "\n"
	print "[$ "+fileResult_text+" $] Current result directory: " + openvas_path
	files = os.listdir(openvas_path)
	print "[$ "+fileResult_text+" $] Openvas files: "
	for file in files:
		if '__init__.py' in file or '__init__.pyc' in file or 'readData.py' in file or 'readData.pyc' in file:
			i=0
		else:
			print file
	print "\n"
	main()

def viewFile():
	type_directoey = raw_input('[$ '+fileResult_text+' $] Select de folder crawler_data or netSecurity_data (1 or 2) > ')
	if '1' in type_directoey or '2' in type_directoey:
		if '1' in type_directoey:
			folder_type = crawler_path
		elif '2' in type_directoey:
			folder_type = netSecurity_path
		name = raw_input('[$ '+fileResult_text+' $] Insert file name with extension > ')
		extension = name.split('.')
		fname = folder_type +"/"+  name
		print "[$ "+fileResult_text+" $] File path: " + fname
		if extension[1] == 'txt': 
			try:
				with open(fname, 'r') as fin:
					print fin.read()
			except:
				print "[$ "+fileResult_text+" $] Error! Try again"
		elif extension[1] == 'csv':
			try:
				comand = 'cat ' + fname
				subprocess.call(comand, shell=True)
			except:
				print '[$ '+fileResult_text+' $] Error! Try again'
	else:
		print('[$ '+fileResult_text+' $] Only 1 or 2 options')
	main()

def updateResultsNetSecurity():
	print('[$ '+fileResult_text+' $] Checking whether crawler files have been created correctly')
	crawler_links_path = crawler_path + "/crawler_links.csv"
	nikto_path = crawler_path + "/nikto_crawler_links.csv"
	nmap_path = crawler_path + "/nmap_crawler.csv"
	geoIP_path = crawler_path + "/geoIP_crawlerIP.csv"
	if os.path.exists(crawler_links_path) and os.path.exists(nikto_path) and os.path.exists(nmap_path) and os.path.exists(geoIP_path):
		print('[$ '+fileResult_text+' $] Checking files has been created correctly!')
		print('[$ '+fileResult_text+' $] Pass to update netSecurity results folder ... ')


options = {'1':viewFiles,'2':viewFile, '3':updateResultsNetSecurity, '0':back}

def main():
	print "\n"
	print "                       - "+menu_text+" -"
	print "               "
	print "               0 : " + back_text
	print "               1 : " + files_folders_text 
	print "               2 : " + result_text
	print "               3 : " + update_text
	print "\n"
	n = raw_input('[$ '+fileResult_text+' $] > ')
	options[n]()