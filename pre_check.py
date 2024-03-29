#!usr/bin/env python

import csv
import sys
import itertools
import os
import time
from telnet_func import telnet_vz
from ssh_func import ssh_vz
import getpass


with open ('just_ip_cat2.csv','rb') as t:
    reader = csv.reader(t)
    ips = list(reader)

flat_list = list(itertools.chain(*ips))

with open('commands_list.csv','rb') as cm:
    reader = csv.reader(cm)
    cms = list(reader)

cmd_list = list(itertools.chain(*cms))

output_text = 'pre_check_scn01.txt'

print flat_list 
print '\n'
print cmd_list
print '\n'

def get_cred():     
	user = str(raw_input("Username: "))     
	pw = getpass.getpass()    
	return {'user' : user, 'password' : pw} 

def main():
	
	cred = get_cred() 	
	user = cred["user"] 	
	pw = cred["password"]

	for ip in flat_list:
	
		try:    
			print ip + ' TELNET'
			telnet_vz(ip,user,pw,cmd_list,output_text)
		
		except:
			try:
				print ip + ' SSH'
				ssh_vz(ip,user,pw,cmd_list,output_text)      
			
			except:
				print ('\n***** No connection to ' + ip + ' ***** \n')
				f = open(output_text,'a')
				f.write('\n***** No connection to ' + ip + ' ***** \n')
				f.write('\n' + '=' * 120 + '\n')
				f.close()

if __name__ == '__main__':
	main()
