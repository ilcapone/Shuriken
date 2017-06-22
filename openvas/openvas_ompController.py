#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# openvas omp controller

import subprocess
import sys
from termcolor import colored, cprint

openvas_text = colored('openvas','red')

exit_text = colored('Exit','blue')
stup_text = colored('Setup','blue')
start_text = colored('Start','blue')
stop_text = colored('Stop','blue')
tasksStatus_text = colored('Tasks status','blue')
ViewTargets_text = colored('View targets','blue')
create_Target_text = colored('Create Target','blue')
createTask_text = colored('Create Task','blue')
startTask_text = colored('Start Task','blue')
getReport_text = colored('Get report Task','blue')
menu_text = colored('OpenVas options','red')

def gass_openvas():
	print "\n"
	print "       ██████╗ ██████╗ ███████╗███╗   ██╗██╗   ██╗ █████╗ ███████╗"
	print "      ██╔═══██╗██╔══██╗██╔════╝████╗  ██║██║   ██║██╔══██╗██╔════╝"
	print "      ██║   ██║██████╔╝█████╗  ██╔██╗ ██║██║   ██║███████║███████╗"
	print "      ██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══██║╚════██║"
	print "      ╚██████╔╝██║     ███████╗██║ ╚████║ ╚████╔╝ ██║  ██║███████║"
	print "       ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝"
	print "\n"

def exit():
	print "[$ "+openvas_text+" $] Back main menu \n"

def openvas_setup():
	gass_openvas()
	print '[$ '+openvas_text+' $] Setup OpenVas'
	try:
		print "[$ "+openvas_text+" $] Waiting openvas set up. This may take a few minutes."
		print "[$ "+openvas_text+" $] ... "
		#result = subprocess.check_output('openvas-setup', shell=True)
		subprocess.call('openvas-setup', shell=True)
		print "[$ "+openvas_text+" $] End setup "

	except Exception,e:
		print "[$ "+openvas_text+" $] Error in setup openvas"
		print str(e)

def openvas_start():
	print '[$ '+openvas_text+' $] Start OpenVas'
	try:
		subprocess.call('openvas-start', shell=True)
		print "[$ "+openvas_text+" $] Ready in https://127.0.0.1:9392"
		
	except Exception,e:
		print "[$ "+openvas_text+" $] Error in start openvas"
		print str(e)
	main()

def openvas_stop():
	print '[$ '+openvas_text+' $] Stop OpenVas'
	try:
		subprocess.call('openvas-stop', shell=True)
		print "[$ "+openvas_text+" $] Stop "
		
	except Exception,e:
		print "[$ "+openvas_text+" $] Error in start openvas"
		print str(e)
	main()

def openvas_getCurrentTask():
	print '[$ '+openvas_text+' $] Get tasks'
	try:
		subprocess.call('omp --config-file=openvas/omp.config -G', shell=True)
		print "[$ "+openvas_text+" $] End get tasks "
		
	except Exception,e:
		print "[$ "+openvas_text+" $] Error in start openvas"
		print str(e)
	main()

def openvas_getCurrentTargets():
	print '[$ '+openvas_text+' $] Get targets'
	try:
		subprocess.call('omp --config-file=openvas/omp.config -T', shell=True)
		print "[$ "+openvas_text+" $] End get targets "
		
	except Exception,e:
		print "[$ "+openvas_text+" $] Error in start openvas"
		print str(e)
	main()

def openvas_creatTarget():
	print '[$ '+openvas_text+' $] Create target'
	try:
		instruccion = "omp --config-file=openvas/omp.config"
		targert_name = raw_input('[$ '+openvas_text+' $] New target name? > ')
		targert_ip = raw_input('[$ '+openvas_text+' $] New target ip? > ')
		xml_instruccion = " --xml '<create_target><name>" + str(targert_name) +"</name><hosts>"+str(targert_ip)+"</hosts></create_target>'"
		omp = instruccion + xml_instruccion
		subprocess.call(omp, shell=True)
	except Exception,e:
		print "[$ "+openvas_text+" $] Error in create target openvas"
		print str(e)
	main()

def openvas_createTask():
	print '[$ '+openvas_text+' $] Create task'
	try:
		instruccion = "omp --config-file=openvas/omp.config"
		task_name = raw_input('[$ '+openvas_text+' $] New task name? > ')		
		subprocess.call('omp --config-file=openvas/omp.config -T', shell=True)
		task_id = raw_input('[$ '+openvas_text+' $] Set task id? > ')
		task_id = '"'+ task_id + '"'
		config_scan = '"' + "daba56c8-73ec-11df-a475-002264764cea" + '"'
		xml_instruccion = " --xml '<create_task><name>"+str(task_name)+"</name><preferences><preference><scanner_name>source_iface</scanner_name><value>eth0</value></preference></preferences><config id="+config_scan+"/><target id="+task_id+"/></create_task>'"
		omp = instruccion + xml_instruccion
		subprocess.call(omp, shell=True)
	except Exception,e:
		print "[$ "+openvas_text+" $] Error in create task openvas"
		print str(e)
	main()

def openvas_startTask():
	print '[$ '+openvas_text+' $] Start task'
	try:
		instruccion = 'omp --config-file=openvas/omp.config -S '
		subprocess.call('omp --config-file=openvas/omp.config -G', shell=True)
		task_id = raw_input('[$ '+openvas_text+' $] Task id? > ')
		omp = instruccion + task_id
		subprocess.call(omp, shell=True)
		print "[$ "+openvas_text+" $] Task is runing in background ... "
		
	except Exception,e:
		print "[$ "+openvas_text+" $] Error in start openvas"
		print str(e)
	main()

def openvas_getReport():
	print '[$ '+openvas_text+' $] Get report of task'
	#onli xml for the moment
	report_format = '5057e5cc-b825-11e4-9d0e-28d24461215b'
	try:
		#subprocess.call('omp --config-file=omp.config --pretty-print --xml="<get_tasks/>"', shell=True)
		subprocess.call('omp --config-file=openvas/omp.config --get-tasks --details', shell=True)
		idTask = raw_input('[$ '+openvas_text+' $] Insert the task id report for extract results > ')
		name_result = raw_input('[$ '+openvas_text+' $] Insert name for the results > ')
		subprocess.call('omp --config-file=openvas/omp.config -R ' + idTask + ' - F ' + report_format + '  > data/openvas/openvas_data_'+name_result+'.xml', shell=True)
		print "[$ "+openvas_text+" $] End get targets "
		
	except Exception,e:
		print "[$ "+openvas_text+" $] Error in start openvas"
		print str(e)
	main()


options = {
'0':exit,
'1':openvas_setup,
'2':openvas_start,
'3':openvas_stop,
'4':openvas_getCurrentTask,
'5':openvas_getCurrentTargets,
'6':openvas_creatTarget,
'7':openvas_createTask,
'8':openvas_startTask,
'9':openvas_getReport}

def main():
	print "\n"
	print "                       - "+menu_text+" -"
	print "                                 "
	print "               0 : " + exit_text
	print "               1 : " + stup_text
	print "               2 : " + start_text
	print "               3 : " + stop_text
	print "               4 : " + tasksStatus_text
	print "               5 : " + ViewTargets_text
	print "               6 : " + create_Target_text
	print "               7 : " + createTask_text
	print "               8 : " + startTask_text
	print "               9 : " + getReport_text
	print "\n"
	try:
		inp = raw_input('[$ '+openvas_text+' $] > ')
		n = str(inp)
		if '0' in n or '1' in n or '2' in n or '3' in n or '4' in n or '5' in n or '6' in n or '7' in n or '8' in n or '9' in n:
			options[n]()
		else:
			print('[$ '+openvas_text+' $] Is not recognized as a valid command')
			main()
	except Exception,e:
		print "Stopping Shuriken"
		print str(e)
		sys.exit()