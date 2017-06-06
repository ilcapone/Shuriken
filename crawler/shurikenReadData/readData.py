#!/usr/bin/python
# -*- coding: utf-8 -*-

# read file resut

import sys
import os
import subprocess

proyect_path = os.getcwd()
data = proyect_path + "/data"
crawler_path = proyect_path + "/data/crawler_data"
netSecurity_path = proyect_path + "/data/netSecurity_data"

def back():
	print "[$ fileResult $] Back main menu \n"

def viewFiles():
	print "[$ fileResult $] Current result directory: " + crawler_path
	files = os.listdir(crawler_path)
	print "[$ fileResult $] Crawler files: "
	for file in files:
		if '__init__.py' in file or '__init__.pyc' in file or 'readData.py' in file or 'readData.pyc' in file:
			i=0
		else:
			print file
	print "\n"
	print "[$ fileResult $] Current result directory: " + netSecurity_path
	files = os.listdir(netSecurity_path)
	print "[$ fileResult $] Net Security files: "
	for file in files:
		if '__init__.py' in file or '__init__.pyc' in file or 'readData.py' in file or 'readData.pyc' in file:
			i=0
		else:
			print file
	print "\n"
	main()

def viewFile():
	type_directoey = raw_input('[$ fileResult $] Select de folder crawler_data or netSecurity_data (1 or 2) > ')
	if '1' in type_directoey or '2' in type_directoey:
		if '1' in type_directoey:
			folder_type = crawler_path
		elif '2' in type_directoey:
			folder_type = netSecurity_path
		name = raw_input('[$ fileResult $] Insert file name with extension > ')
		extension = name.split('.')
		fname = folder_type +"/"+  name
		print "[$ fileResult $] File path: " + fname
		if extension[1] == 'txt': 
			try:
				with open(fname, 'r') as fin:
					print fin.read()
			except:
				print "[$ fileResult $] Error! Try again"
		elif extension[1] == 'csv':
			try:
				comand = 'cat ' + fname
				subprocess.call(comand, shell=True)
			except:
				print '[$ fileResult $] Error! Try again'
	else:
		print('[$ fileResult $] Only 1 or 2 options')
	main()

def updateResultsNetSecurity():
	print('[$ fileResult $] Only 1 or 2 options')

options = {'1':viewFiles,'2':viewFile, '3':updateResultsNetSecurity, '0':back}

def main():
	print "\n"
	print "                       - fileResult Options -"
	print "               "
	print "               0 : Back"
	print "               1 : View files in folder"
	print "               2 : View result content"
	print "               3 : Update netSecurity results"
	print "\n"
	n = raw_input('[$ fileResult $] > ')
	options[n]()