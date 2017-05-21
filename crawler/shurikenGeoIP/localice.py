#!/usr/bin/python
# -*- coding: utf-8 -*-

# localice

import GeoIP
import csv
import os

ip_list=['init']
geo_ip_list = []
shuriken_path = os.getcwd()
dictionary = shuriken_path + "/crawler/shurikenGeoIP/GeoLiteCity.dat"
data = shuriken_path + "/crawler/data/geoIP_specificIP.csv"
data_crawler = shuriken_path + "/crawler/data/geoIP_crawlerIP.csv"
nikto_data = shuriken_path + "/crawler/data/nikto_crawler_links.csv"

def back():
	print "[$ geo-ip $] Back main menu \n"

def specific_IP():
	print "[$ geo-ip $] Specific geo IP"
	ip = raw_input('[$ geo-ip $] Insert ip > ')
	gi = GeoIP.open(dictionary, GeoIP.GEOIP_INDEX_CACHE | GeoIP.GEOIP_CHECK_CACHE)
	geoInfo = gi.record_by_name(ip)
	with open(data, 'wb') as f:
		w = csv.DictWriter(f, geoInfo.keys())
		w.writeheader()
		w.writerow(geoInfo)

def crawler_IP():
	print "[$ geo-ip $] Crawler"
	print "[$ geo-ip $] Open data/nikto_crawler_links.csv"
	fName= nikto_data
	firstWrite = True
	if os.path.exists(fName):
		with open(fName, 'rU') as f:
			try:
				reader = csv.reader(f)
				for row in reader:
					if len(row)!= 1:
						print "[$ geo-ip $] Cuerren reader IP :" + row[1]
						check_current_url(row[1])
			except Exception as e:
				print "[$ geo-ip $] Error reading data/nikto_crawler_links.csv"
				print e
			try:
				print "[$ geo-ip $] Writing ..."
				write_geoIP_crawler()
			except Exception as e:
				print "[$ geo-ip $] Error writing data/geoIP_crawlerIP.csv"
				print e
	else:
		print "[$ geo-ip $] The file data/nikto_crawler_links.csv don't exist, please first run nikto crawler"
	print "[$ geo-ip $] Output file geoIP_crawlerIP.csv in /data forlder"

def check_current_url(curr_ip):
	checker = False
	for ip in ip_list:
		if ip == curr_ip:
			checker = True
	if checker:
		print "[$ geo-ip $] The ip " + curr_ip + " has already been geolocalice"
	else:		
		print "[$ geo-ip $] The url " + curr_ip + " has not been geolocalice"
		ip_list.insert(len(ip_list),curr_ip)
		launch_geoIP_crawler(curr_ip)

def launch_geoIP_crawler(ip):
	gi = GeoIP.open(dictionary, GeoIP.GEOIP_INDEX_CACHE | GeoIP.GEOIP_CHECK_CACHE)
	geoInfo = gi.record_by_name(ip)
	geoInfo['ip'] = ip
	geo_ip_list.insert(len(geo_ip_list),geoInfo)

def write_geoIP_crawler():
	print geo_ip_list
	first = True
	with open(data_crawler, 'a') as f:
		for gIP in geo_ip_list:
			if first:
				w = csv.DictWriter(f, gIP.keys())
				w.writeheader()
				w.writerow(gIP)
				first = False
			else:
				if gIP is not None:
					w.writerow(gIP)

options = {'0':specific_IP,'1':crawler_IP, '2':back}

def main():
	print "                       - geoIP Options -"
	print "               0 : Specific geoIP"
	print "               1 : Crawler geoIP"
	print "               2 : Back"
	print "\n"
	n = raw_input('[$ geo-ip $] > ')
	options[n]()