import sys
import nmap
import os
import csv

ip_list=['init']
shuriken_path = os.getcwd()
data = shuriken_path + "/crawler/data/nmap_crawler.csv"
nikto_data = shuriken_path + "/crawler/data/nikto_crawler_links.csv"
csvwriter = open(data, "w")
proxy_check = None

def crawler_nmap():
	print "[$ nmap $] Start crawler nmap module"
	print "[$ nmap $] Open data/nikto_crawler_links.csv"
	fName= nikto_data
	if os.path.exists(fName):
		with open(fName, 'rU') as f:
			try:
				reader = csv.reader(f)
				print "[$ nmap $] reading. ."
				for row in reader:
					if len(row) > 1:
						check_current_ip(row[1])
			except :
				print "[$ nmap $] Error rading data/nikto_crawler_links.csv"
	else:
		print "[$ nmap $] The file data/nikto_crawler_links.csv don't exist, please first extract de web vulnerabilitys with nikto"
	print "[$ nmap $] Output file nmap_crawler.csv"

def check_current_ip(curr_ip):
	checker = False
	for ip in ip_list:
		if ip == curr_ip:
			checker = True
	if checker!=True:		
		print "[$ nmap $] Start scaning against ip " + curr_ip
		ip_list.insert(len(ip_list),curr_ip)
		evade_ids_crwler(curr_ip)

def evade_ids_crwler(current_ip):
	nm = nmap.PortScanner()
	ip = current_ip
	portRank = '0-65535'
	args = '--spoof-mac Cisco -T4 --source-port 53 -sS --send-ip -n --data-length 30 --randomize-hosts -n -f -f -sV --version-all -O'
	if proxy_check is None:
		px = raw_input('[$ nmap $] You want to use proxy? (y/n) > ')
		proxy_check = px
	if proxy_check == 'y':
		ip_port = raw_input('[$ nmap $] Insert IP:PORT > ')
		proxy = '--proxy http://'+ str(ip_port)
		print "[$ nmap $] Start nmap with proxy " + ip_port
		print "[$ nmap $] arguments : " + args
		args = args + " " + proxy
		nm.scan(ip, portRank, arguments = args)
	else:
		print "[$ nmap $] arguments : " + args
		nm.scan(ip, portRank, arguments = args)
	print nm.csv()
	csvwriter.write(nm.csv())
	print "[$ nmap $] End scan"