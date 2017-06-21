#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# openvas omp controller

import subprocess
import sys

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
	print "[$ openvas $] Back main menu \n"

def openvas_setup():
	gass_openvas()
	print '[$ openvas $] Setup OpenVas'
	try:
		print "[$ openvas $] Waiting openvas set up. This may take a few minutes."
		print "[$ openvas $] ... "
		#result = subprocess.check_output('openvas-setup', shell=True)
		subprocess.call('openvas-setup', shell=True)
		print "[$ openvas $] End setup "

	except Exception,e:
		print "[$ openvas $] Error in setup openvas"
		print str(e)

def openvas_start():
	print '[$ openvas $] Start OpenVas'
	try:
		subprocess.call('openvas-start', shell=True)
		print "[$ openvas $] Ready "
		
	except Exception,e:
		print "[$ openvas $] Error in start openvas"
		print str(e)

def openvas_stop():
	print '[$ openvas $] Stop OpenVas'
	try:
		subprocess.call('openvas-stop', shell=True)
		print "[$ openvas $] Stop "
		
	except Exception,e:
		print "[$ openvas $] Error in start openvas"
		print str(e)

def openvas_getCurrentTask():
	print '[$ openvas $] Get tasks'
	try:
		subprocess.call('omp --config-file=openvas/omp.config -G', shell=True)
		print "[$ openvas $] End get tasks "
		
	except Exception,e:
		print "[$ openvas $] Error in start openvas"
		print str(e)

def openvas_getCurrentTargets():
	print '[$ openvas $] Get targets'
	try:
		subprocess.call('omp --config-file=openvas/omp.config -T', shell=True)
		print "[$ openvas $] End get targets "
		
	except Exception,e:
		print "[$ openvas $] Error in start openvas"
		print str(e)

def openvas_creatTarget():
	print '[$ openvas $] Create target'
	try:
		instruccion = "omp --config-file=openvas/omp.config"
		targert_name = raw_input('[$ openvas $] New target name? > ')
		targert_ip = raw_input('[$ openvas $] New target ip? > ')
		xml_instruccion = " --xml '<create_target><name>" + str(targert_name) +"</name><hosts>"+str(targert_ip)+"</hosts></create_target>'"
		omp = instruccion + xml_instruccion
		subprocess.call(omp, shell=True)
	except Exception,e:
		print "[$ openvas $] Error in create target openvas"
		print str(e)

def openvas_createTask():
	print '[$ openvas $] Create task'
	try:
		instruccion = "omp --config-file=openvas/omp.config"
		task_name = raw_input('[$ openvas $] New task name? > ')		
		subprocess.call('omp --config-file=openvas/omp.config -T', shell=True)
		task_id = raw_input('[$ openvas $] Set task id? > ')
		task_id = '"'+ task_id + '"'
		config_scan = '"' + "daba56c8-73ec-11df-a475-002264764cea" + '"'
		xml_instruccion = " --xml '<create_task><name>"+str(task_name)+"</name><preferences><preference><scanner_name>source_iface</scanner_name><value>eth0</value></preference></preferences><config id="+config_scan+"/><target id="+task_id+"/></create_task>'"
		omp = instruccion + xml_instruccion
		subprocess.call(omp, shell=True)
	except Exception,e:
		print "[$ openvas $] Error in create task openvas"
		print str(e)

def openvas_startTask():
	print '[$ openvas $] Start task'
	try:
		instruccion = 'omp --config-file=openvas/omp.config -S '
		subprocess.call('omp --config-file=openvas/omp.config -G', shell=True)
		task_id = raw_input('[$ openvas $] Task id? > ')
		omp = instruccion + task_id
		subprocess.call(omp, shell=True)
		print "[$ openvas $] Task is runing in background ... "
		
	except Exception,e:
		print "[$ openvas $] Error in start openvas"
		print str(e)

def openvas_getReport():
	print '[$ openvas $] Get report of task'
	#onli xml for the moment
	report_format = '5057e5cc-b825-11e4-9d0e-28d24461215b'
	try:
		#subprocess.call('omp --config-file=omp.config --pretty-print --xml="<get_tasks/>"', shell=True)
		subprocess.call('omp --config-file=openvas/omp.config --get-tasks --details', shell=True)
		idTask = raw_input('[$ openvas $] Insert the task id report for extract results > ')
		name_result = raw_input('[$ openvas $] Insert name for the results > ')
		subprocess.call('omp --config-file=openvas/omp.config -R ' + idTask + ' - F ' + report_format + '  > data/openvas/openvas_data_'+name_result+'.xml', shell=True)
		print "[$ openvas $] End get targets "
		
	except Exception,e:
		print "[$ openvas $] Error in start openvas"
		print str(e)


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
	print "                       - OpenVas options -"
	print "                                 "
	print "               0 : Exit"
	print "               1 : Setup"
	print "               2 : Start"
	print "               3 : Stop"
	print "               4 : Tasks status"
	print "               5 : View targets"
	print "               6 : Create Target"
	print "               7 : Create Task"
	print "               8 : Start Task"
	print "               9 : Get report Task"
	print "\n"
	try:
		inp = raw_input('[$ openvas $] > ')
		n = str(inp)
		if '0' in n or '1' in n or '2' in n or '3' in n or '4' in n or '5' in n or '6' in n or '7' in n or '8' in n or '9' in n:
			options[n]()
		else:
			print('[$ openvas $] Is not recognized as a valid command')
			main()
	except Exception,e:
		print "Stopping Shuriken"
		print str(e)
		sys.exit()