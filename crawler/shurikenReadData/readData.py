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
	selected = raw_input('[$ '+fileResult_text+' $] Load crawler or openvas (0 : Crawler , 1 : Openvas) > ')
	if '0' in selected:
		print('[$ '+fileResult_text+' $] Crawler results')
		files = os.listdir(crawler_path)
		for file in files:
			if '__init__.py' in file or '__init__.pyc' in file or 'readData.py' in file or 'readData.pyc' in file:
				pass
			else:
				if '.csv' in file:
					pass
				else:
					files_subfolder = os.listdir(crawler_path + "/" + file)
					subfoler = colored('Subfoler > ' + file,'yellow')
					print(subfoler)
		print "\n"
		select_result = raw_input('[$ '+fileResult_text+' $] Insert subfolder to loan in Net.Security > ')
		directory = crawler_path + "/" + str(select_result)
		if os.path.exists(directory):
			print('[$ '+fileResult_text+' $] Cleaning Net.Security data ... ')
			comand = 'rm '+ netSecurity_path + "/crawler_links.csv"
			subprocess.call(comand, shell=True)
			comand = 'rm '+ netSecurity_path + "/nikto_crawler_links.csv"
			subprocess.call(comand, shell=True)
			comand = 'rm '+ netSecurity_path + "/nmap_crawler.csv"
			subprocess.call(comand, shell=True)
			comand = 'rm '+ netSecurity_path + "/geoIP_crawlerIP.csv"
			subprocess.call(comand, shell=True)
			print('[$ '+fileResult_text+' $] Loan new content in Net.Security')
			comand = 'cp '+ directory + "/crawler_links.csv " + netSecurity_path
			subprocess.call(comand, shell=True)
			comand = 'cp '+ directory + "/nikto_crawler_links.csv " + netSecurity_path
			subprocess.call(comand, shell=True)
			comand = 'cp '+ directory + "/nmap_crawler.csv " + netSecurity_path
			subprocess.call(comand, shell=True)
			comand = 'cp '+ directory + "/geoIP_crawlerIP.csv " + netSecurity_path
			subprocess.call(comand, shell=True)
		else:
			print('[$ '+fileResult_text+' $] Subfolder ' + select_result + ' doesnt exist')
	elif '1' in selected:
		print('[$ '+fileResult_text+' $] Openvas results')
		files = os.listdir(openvas_path)
		for file in files:
			if '__init__.py' in file or '__init__.pyc' in file or 'readData.py' in file or 'readData.pyc' in file:
				pass
			else:
				print file
		print "\n"
		select_result = raw_input('[$ '+fileResult_text+' $] Insert file to loan in Net.Security > ')
		directory = openvas_path + "/" + str(select_result)
		if os.path.exists(directory):
			print('[$ '+fileResult_text+' $] Cleaning Net.Security data ... ')
			comand = 'rm '+ netSecurity_path + "/openvas/" + select_result
			subprocess.call(comand, shell=True)
			comand = 'cp '+ directory + " " + netSecurity_path + "/openvas"
			subprocess.call(comand, shell=True)
		else:
			print('[$ '+fileResult_text+' $] File ' + select_result + ' doesnt exist')
	main()


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