#!/usr/bin/python
# -*- coding: utf-8 -*-

# read file resut

import sys
import os
import subprocess

def back():
	print "[$ fileResult $] Back main menu \n"

def viewFiles():
	path = os.getcwd() + "/data"
	print "[$ fileResult $] Current result directory: " + path
	files = os.listdir(path)
	print "\n"
	for file in files:
		if '__init__.py' in file or '__init__.pyc' in file or 'readData.py' in file or 'readData.pyc' in file:
			i=0
		else:
			print file
	main()

def viewFile():
	name = raw_input('[$ fileResult $] Insert file name with extension > ')
	extension = name.split('.')
	fname = "data/" + name
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
	main()

options = {'0':viewFiles,'1':viewFile, '2':back}

def main():
	print "\n"
	print "                       - fileResult Options -"
	print "               0 : View files in folder"
	print "               1 : View result content"
	print "               2 : Back"
	print "\n"
	n = raw_input('[$ fileResult $] > ')
	options[n]()