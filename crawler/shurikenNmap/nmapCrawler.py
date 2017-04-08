import sys
import nmap
import os
import csv

ip_list=['init']
csvwriter = open('data/nmap_crawler.csv', "w")

def crawler_nmap():
	print "[$ nmap $] Start crawler nmap module"
	print "[$ nmap $] Open data/nikto_crawler_links.csv"
	fName= 'data/nikto_crawler_links.csv'
	if os.path.exists(fName):
		with open(fName, 'r') as f:
			#try:
				reader = csv.reader(f)
				print "[$ nmap $] reading. ."
				for row in reader:
					if len(row) > 1:
						check_current_ip(row[1])
			#except :
				#print "[$ nmap $] Error rading data/crawler_links.csv"
	else:
		print "[$ nmap $] The file data/crawler_links.csv don't exist, please first extract de web vulnerabilitys with nikto"
	print "[$ nmap $] Output file nmap_crawler.csv"

def check_current_ip(curr_ip):
	checker = False
	for ip in ip_list:
		if ip == curr_ip:
			checker = True
	if checker!=True:		
		print "[$ nmap $] The ip " + curr_ip + " has not been scanned"
		ip_list.insert(len(ip_list),curr_ip)
		evade_ids_crwler(curr_ip)

def evade_ids_crwler(current_ip):
	nm = nmap.PortScanner()
	ip = current_ip
	portRank = '0-65535'
	print "[$ nmap $] --spoof-mac Cisco -T4 --source-port 53 -sS --send-ip -n --data-length 30 --randomize-hosts -n -f -f -sV --version-all -O"
	nm.scan(ip, arguments='--spoof-mac Cisco -T4 --source-port 53 -sS --send-ip -n --data-length 30 --randomize-hosts -n -f -f -sV --version-all -O')
	print nm.csv()
	csvwriter.write(nm.csv())
	print "[$ nmap $] End scan"
